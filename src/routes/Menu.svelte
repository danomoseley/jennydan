<script>
    import { fly, scale } from 'svelte/transition';
    import { quadOut } from 'svelte/easing';
    import '@fontsource-variable/bodoni-moda';
    import '@fontsource-variable/montserrat';

    export let open;
</script>

{#if open}
    <div class="menu">
        {#each [{title:'Wedding Weekend',link:'/'}, {title:'Schedule',link:'/schedule'},{title:'Getting To Cooperstown',link:'/travel'},{title:'Things To Do','link':'/things-to-do'},{title:'Frequently Asked Questions','link':'/faq'},{title:'Our Registry','link':'/registry'},{title:'Accommodations','link':'/accommodations'}] as link, i}
            <p transition:fly={{ y: -15, delay: 50 * i }}>
                <a href={link.link}>{link.title}</a>
            </p>
        {/each}
    </div>

    <div class="bar" transition:scale={{ duration: 750, easing: quadOut, opacity: 1 }} />
{/if}

<style>
    .menu {
        text-align: center;
        font-size: 1em;
        letter-spacing: 0.15em;
        padding: 1em;
        padding-top: 0;
    }
    p {
        cursor: pointer;
        width: max-content;
        margin: 1rem auto;
    }
    p:hover {
        text-decoration: underline;
    }
    .bar {
        border-top: 1px solid rgb(30,87,134);
        height: 0;
    }
    a {
        text-decoration: none;
        color: rgb(30,87,134);
    }
</style>