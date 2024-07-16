<svelte:head>
  <title>Choose Your Meals - Jenny & Dan</title>
  <meta name="description" content="Please choose your meal for our wedding." />
</svelte:head>

<script lang="ts">
  import type { PageData } from './$types';
  export let data: PageData;
</script>
<div id="rsvp">
  <h2>Reception Meal Choice</h2>
  <form method="POST">
    {#each data.rsvp_guests as rsvp_guest}
      <h3>- {rsvp_guest.first_name} {rsvp_guest.last_name} -</h3>
      <ul>
        <li>
          <div class="radio-flex">
            <input
              name="meal-choice-{rsvp_guest.rowid}"
              id="meal-choice-{rsvp_guest.rowid}-1"
              value={1}
              type="radio"
              required
              bind:group={rsvp_guest.meal_choice_rowid} />
            <label for="meal-choice-{rsvp_guest.rowid}-1">Chicken</label>
          </div>
        </li>
        <li>
          <div class="radio-flex">
            <input
              name="meal-choice-{rsvp_guest.rowid}"
              id="meal-choice-{rsvp_guest.rowid}-2"
              value={2}
              type="radio"
              required
              bind:group={rsvp_guest.meal_choice_rowid} />
            <label for="meal-choice-{rsvp_guest.rowid}-2">Beef</label>
          </div>
        </li>
        <li>
          <div class="radio-flex">
            <input
              name="meal-choice-{rsvp_guest.rowid}"
              id="meal-choice-{rsvp_guest.rowid}-3"
              value={3}
              type="radio"
              required
              bind:group={rsvp_guest.meal_choice_rowid} />
            <label for="meal-choice-{rsvp_guest.rowid}-3">Vegetarian</label>
          </div>
        </li>
        <li>
          <div class="radio-flex">
            <input
              name="meal-choice-{rsvp_guest.rowid}"
              id="meal-choice-{rsvp_guest.rowid}-4"
              value={4}
              type="radio"
              required
              bind:group={rsvp_guest.meal_choice_rowid} />
            <label for="meal-choice-{rsvp_guest.rowid}-4">Kids Choice - Chicken Nuggets</label>
          </div>
        </li>
      </ul>
    {/each}
    <input class="button" type="submit" value="Submit">
</div>