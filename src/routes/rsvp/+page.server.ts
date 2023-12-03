import { fail } from '@sveltejs/kit';
import { z } from 'zod';
import { message, setError, superValidate } from 'sveltekit-superforms/server';


const rsvpSchema = z.object({
  email: z.string().trim().email().min(1),
  first_name: z.string().trim().min(1),
  last_name: z.string().trim().min(1),
  attending: z.boolean().default(true),
  num_attending: z.union([z.coerce.number().int().positive(), z.nan()]).optional(),
  guest_names: z.string().optional(),
  dietary_restrictions: z.string().optional()
}).superRefine(({ attending, num_attending, guest_names }, refinementContext) => {
    if (attending) {
        if ( !num_attending ) {
            return refinementContext.addIssue({
                code: z.ZodIssueCode.custom,
                message: 'This field is required',
                path: ['num_attending']
            })
        } else if ( num_attending > 1 && !guest_names) {
            return refinementContext.addIssue({
                code: z.ZodIssueCode.custom,
                message: 'Please provide additional guest names',
                path: ['guest_names']
            })
        }
    }
});

export const load = (async () => {
  const form = await superValidate(rsvpSchema);
  return { form };
});

/** @type {import('./$types').Actions} */
export const actions = {
    default: async ({ request, platform }) => {
        const form = await superValidate(request, rsvpSchema);
        if (!form.valid) {
            return fail(400, { form });
        }
        let result = await platform.env.DB.prepare(
            "SELECT * FROM rsvp WHERE email = ?1"
        ).bind(form.data.email).run();
        if (result.results.length) {
            return setError(form, 'email', 'E-mail already exists.');
        }

        result = await platform.env.DB.prepare(
            "INSERT INTO rsvp (attending, email, first_name, last_name, num_attending, guest_names, dietary_restrictions) VALUES (?1, ?2, ?3, ?4, ?5, ?6, ?7)"
        ).bind(+ form.data.attending, form.data.email, form.data.first_name, form.data.last_name, form.data.num_attending ?? null, form.data.guest_names ?? null, form.data.dietary_restrictions ?? null).run();
        return message(form, 'Thank you for RSVPing!');
    }
};