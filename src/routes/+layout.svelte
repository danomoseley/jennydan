<script>
  import './styles.css';

  import { Hamburger } from 'svelte-hamburgers';
  import Menu from './Menu.svelte';

  let open;
</script>
<div class="header">
  <div class="left">
    <Hamburger bind:open --color="rgb(30,87,134)" />
  </div>
  <div class="center">
    Jenny & Dan
  </div>
  <div class="right">
  </div>
</div>

<Menu bind:open />
<div id="content">
  <slot></slot>
</div>
