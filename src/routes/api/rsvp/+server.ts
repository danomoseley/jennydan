import type { RequestHandler } from "@sveltejs/kit";

/** @type {import('@sveltejs/kit').RequestHandler} */
export async function GET({ request, platform }) {
  let result = await platform.env.DB.prepare(
    "SELECT * FROM rsvp LIMIT 5"
  ).run();
  return new Response(JSON.stringify(result));
}

/** @type {import('@sveltejs/kit').RequestHandler} */
export async function POST({ request, platform }) {
  const data = await request.formData();
  const email = data.get('email')
  const first_name = data.get('first_name')
  const last_name = data.get('last_name')
  const num_attending = data.get('num_attending')

  let result = await platform.env.DB.prepare(
    "INSERT INTO rsvp (email, first_name, last_name, num_attending) VALUES (?1, ?2, ?3, ?4)"
  ).bind(email, first_name, last_name, num_attending).run();
  return new Response(JSON.stringify(result));
}