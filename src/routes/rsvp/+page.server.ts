import { fail } from '@sveltejs/kit';
import { z } from 'zod';
import { message, setError, superValidate } from 'sveltekit-superforms/server';


const rsvpSchema = z.object({
  email: z.string().trim().email().min(1),
  first_name: z.string().trim().min(1),
  last_name: z.string().trim().min(1),
  num_attending: z.coerce.number().positive().default(null)
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
            "INSERT INTO rsvp (email, first_name, last_name, num_attending) VALUES (?1, ?2, ?3, ?4)"
        ).bind(form.data.email, form.data.first_name, form.data.last_name, form.data.num_attending).run();
        return message(form, 'Thank you for RSVPing!');
    }
};