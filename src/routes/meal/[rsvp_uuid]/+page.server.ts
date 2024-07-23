import { error, fail, redirect } from '@sveltejs/kit';

/** @type {import('./$types').PageServerLoad} */
export async function load({ params, platform }) {
    let result = await platform.env.DB.prepare(
            "SELECT rsvp_guest.rowid, rsvp_guest.* FROM rsvp_guest JOIN rsvp ON rsvp.rowid = rsvp_guest.rsvp_rowid WHERE rsvp.uuid = ?1"
        ).bind(params.rsvp_uuid).run()
    if (result.results.length == 0) {
        throw error(404, {
            message: 'RSVP Not Found'
        });
    }
    return {
        rsvp_guests: result.results
    };
}

/** @type {import('./$types').Actions} */
export const actions = {
    default: async ({ request, params, platform }) => {
        const data = await request.formData();
        for (var data_pair of data.entries()) {
            var regex = /meal-choice-(\d+)/g;
            var regex_result = regex.exec(data_pair[0]);
            if (regex_result) {
                let result = await platform.env.DB.prepare(
                    "SELECT * FROM rsvp JOIN rsvp_guest ON rsvp.rowid = rsvp_guest.rsvp_rowid WHERE rsvp.uuid = ?1 AND rsvp_guest.rowid = ?2"
                ).bind(params.rsvp_uuid, regex_result[1]).run();
                if (!result.results.length) {
                    return fail(400);
                }
                result = await platform.env.DB.prepare(
                    "UPDATE rsvp_guest set meal_choice_rowid = ?1 WHERE rowid=?3"
                ).bind(data_pair[1], params.rsvp_uuid, regex_result[1]).run();
            }
        }
        throw redirect(303, '/meal-thank-you');
    }
};