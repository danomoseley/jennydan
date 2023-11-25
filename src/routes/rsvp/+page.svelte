<svelte:head>
  <title>Dan & Jenny Are Getting Married! August 17, 2024</title>
  <meta name="description" content="Dan & Jenny Are Getting Married! August 17, 2024 in Cooperstown, NY." />
</svelte:head>

<form action="/api/rsvp" method="POSt">
    <label for="email">Email:</label>
    <input name="email" type="text" id="email"><br/>
    <label for="first_name">First Name:</label>
    <input name="first_name" type="text" id="first_name"><br/>
    <label for="last_name">Last Name:</label>
    <input name="last_name" type="text" id="last_name"><br/>
    <label for="last_name">Number Attending:</label>
    <input name="num_attending" type="text" id="num_attending"><br/>
    <input type="submit" value="Submit">
</form>