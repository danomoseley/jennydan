<svelte:head>
  <title>Choose Your Meals - Jenny & Dan</title>
  <meta name="description" content="Please choose your meal for our wedding reception." />
</svelte:head>

<script lang="ts">
  import type { PageData } from './$types';
  export let data: PageData;
</script>
<div id="rsvp">
  <h2>Reception Meal Choice</h2>
  All adult options served with a side of roasted local vegetables and baby gold potatoes.
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
            <label for="meal-choice-{rsvp_guest.rowid}-1">Chicken Francese</label>
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
            <label for="meal-choice-{rsvp_guest.rowid}-2">Prime Rib</label>
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
            <label for="meal-choice-{rsvp_guest.rowid}-3">Grilled Herb Crusted Salmon with Mango Salsa</label>
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
            <label for="meal-choice-{rsvp_guest.rowid}-4">Eggplant Rollatini (vegetarian and gluten free)</label>
          </div>
        </li>
        <li>
          <div class="radio-flex">
            <input
              name="meal-choice-{rsvp_guest.rowid}"
              id="meal-choice-{rsvp_guest.rowid}-5"
              value={5}
              type="radio"
              required
              bind:group={rsvp_guest.meal_choice_rowid} />
            <label for="meal-choice-{rsvp_guest.rowid}-5">Kids Choice - Chicken Fingers with fries</label>
          </div>
        </li>
        <li>
          <div class="radio-flex">
            <input
              name="meal-choice-{rsvp_guest.rowid}"
              id="meal-choice-{rsvp_guest.rowid}-6"
              value={6}
              type="radio"
              required
              bind:group={rsvp_guest.meal_choice_rowid} />
            <label for="meal-choice-{rsvp_guest.rowid}-6">Infant / None</label>
          </div>
        </li>
      </ul>
    {/each}
    <input class="button" type="submit" value="Submit">
</div>