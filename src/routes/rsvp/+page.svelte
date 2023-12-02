<svelte:head>
  <title>Dan & Jenny Are Getting Married! August 17, 2024</title>
  <meta name="description" content="Dan & Jenny Are Getting Married! August 17, 2024 in Cooperstown, NY." />
</svelte:head>

<script lang="ts">
  import type { PageData } from './$types';
  import { superForm } from 'sveltekit-superforms/client';
  export let data: PageData;
  const { allErrors, constraints, enhance, errors, form, message } = superForm(data.form);
</script>
<div id="rsvp">
  <h2>RSVP</h2>
  {#if $message}
    <div class="message">{$message}</div>
  {:else}
      {#if $allErrors.length}
        <ul>
          {#each $allErrors as error}
            <li>
              <b>{error.path}:</b>
              {error.messages.join('. ')}
            </li>
          {/each}
        </ul>
      {/if}
      <form method="POST" use:enhance>
        <ul>
          <li>
            <label for="email">Email</label>
            <input
                name="email"
                type="email"
                required
                aria-invalid={$errors.email ? 'true' : undefined}
                bind:value={$form.email}
                {...$constraints.email} />
            {#if $errors.email}<span class="invalid">{$errors.email}</span>{/if}
          </li>
          <li>
            <label for="first_name">First Name</label>
            <input
                name="first_name"
                type="text"
                required
                aria-invalid={$errors.first_name ? 'true' : undefined}
                bind:value={$form.first_name}
                {...$constraints.first_name} />
            {#if $errors.first_name}<br/><span class="invalid">{$errors.first_name}</span>{/if}
          </li>
          <li>
            <label for="last_name">Last Name</label>
            <input
                name="last_name"
                type="text"
                required
                aria-invalid={$errors.last_name ? 'true' : undefined}
                bind:value={$form.last_name}
                {...$constraints.last_name} />
            {#if $errors.last_name}<br/><span class="invalid">{$errors.last_name}</span>{/if}
          </li>
          <li>
            <label for="num_attending">Number Attending</label>
            <input
                name="num_attending"
                type="number"
                required
                bind:value={$form.num_attending}
                {...$constraints.num_attending} />
            {#if $errors.num_attending}<br/><span class="invalid">{$errors.num_attending}</span>{/if}
          <li>
          <li>
            <input type="submit" value="Submit">
          </li>
        </ul>
      </form>
      <style>
        .invalid {
          color: red;
        }
      </style>
  {/if}
</div>