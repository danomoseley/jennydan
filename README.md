Wedding website of Jenny & Dan.
August 17, 2024 in Cooperstown, NY.

Created in SvelteKit on Cloudflare Pages using Cloudflare D1.

## Developing

To run in dev mode:
```bash
npm run dev
```

To test with D1:
```
npm run build && npx wrangler pages dev .svelte-kit/cloudflare --d1=D1_DATABASE_NAME
```

## Building

To create a production version of your app:

```bash
npm run build
```

Commits are automatically deployed on Cloudflare Pages