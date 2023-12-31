<svelte:head>
  <title>RSVP - Jenny & Dan</title>
  <meta name="description" content="Let us know if you think you will attend our wedding to help us in planning." />
</svelte:head>

<script lang="ts">
  import type { PageData } from './$types';
  import { superForm } from 'sveltekit-superforms/client';
  export let data: PageData;
  const { allErrors, constraints, enhance, errors, form, message } = superForm(data.form);
  let extendedHidden = false;
  let additionalGuestsHidden = true;
  function toggleHidden() {
    extendedHidden = !extendedHidden;
  }
  function numAttendingChanged() {
    if (event.currentTarget.value > 1) {
      additionalGuestsHidden = false;
    } else {
      additionalGuestsHidden = true;
    }
  }
</script>
<div id="rsvp">
  <h2>RSVP</h2>
  {#if $message}
    <div class="message">{$message}</div>
  {:else}
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
            <label for="first_name">First name</label>
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
            <label for="last_name">Last name</label>
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
            <label for="attending">Will you be attending?</label>
            <div class="radio-flex">
              <input
                name="attending"
                id="attending-true"
                value={true}
                type="radio"
                required
                bind:group={$form.attending}
                on:change={toggleHidden}
                {...$constraints.attending} />
              <label for="attending-true">Yes!</label>
            </div>
            <div class="radio-flex">
              <input
                name="attending"
                id="attending-false"
                value={false}
                type="radio"
                bind:group={$form.attending}
                on:change={toggleHidden}
                {...$constraints.attending} />
              <label for="attending-false">No, unfortunately</label>
              <br/>
            </div>
            {#if $errors.attending}<span class="invalid">{$errors.attending}</span>{/if}
          </li>
          <li hidden={extendedHidden}>
            <ul>
              <li>
                <label for="num_attending">Number attending (including children)</label>
                <input
                    name="num_attending"
                    type="number"
                    bind:value={$form.num_attending}
                    on:keyup={numAttendingChanged}
                    {...$constraints.num_attending} />
                {#if $errors.num_attending}<br/><span class="invalid">{$errors.num_attending}</span>{/if}
              </li>
              <li hidden={additionalGuestsHidden}>
                <label for="guest_names">Additional guest names</label>
                <textarea
                    name="guest_names"
                    aria-invalid={$errors.guest_names ? 'true' : undefined}
                    bind:value={$form.guest_names}
                    {...$constraints.guest_names} />
                {#if $errors.guest_names}<br/><span class="invalid">{$errors.guest_names}</span>{/if}
              </li>
              <li>
                <label for="dietary_restrictions">Dietary restrictions</label>
                <textarea
                    name="dietary_restrictions"
                    aria-invalid={$errors.dietary_restrictions ? 'true' : undefined}
                    bind:value={$form.dietary_restrictions}
                    {...$constraints.dietary_restrictions} />
                {#if $errors.dietary_restrictions}<br/><span class="invalid">{$errors.dietary_restrictions}</span>{/if}
              </li>
              <li>
                <label for="attending">Plan on attending the morning after brunch?</label>
                <div class="radio-flex">
                  <input
                    name="attending_brunch"
                    id="attending-brunch-true"
                    value={true}
                    type="radio"
                    required
                    bind:group={$form.attending_brunch}
                    {...$constraints.attending_brunch} />
                  <label for="attending-brunch-true">Yes!</label>
                </div>
                <div class="radio-flex">
                  <input
                    name="attending_brunch"
                    id="attending-brunch-false"
                    value={false}
                    type="radio"
                    bind:group={$form.attending_brunch}
                    {...$constraints.attending_brunch} />
                  <label for="attending-brunch-false">No</label>
                  <br/>
                </div>
                {#if $errors.attending_brunch}<span class="invalid">{$errors.attending_brunch}</span>{/if}
              </li>
            </ul>
          </li>
          <li>
            <input class="button" type="submit" value="Submit">
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