<script>
    import { fly, scale } from 'svelte/transition';
    import { quadOut } from 'svelte/easing';
    import '@fontsource-variable/bodoni-moda';
    import '@fontsource-variable/montserrat';

    export let open;
</script>

{#if open}
    <div class="menu">
        {#each [{title:'Welcome',link:'/'}, {title:'RSVP',link:'/rsvp'}, {title:'Schedule',link:'/schedule'}, {title:'Getting Here',link:'/travel'},{title:'Accommodations','link':'accommodations'},{title:'Things To Do','link':'things-to-do'},{title:'FAQ','link':'faq'}] as link, i}
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
        border-style: solid;
        border-color: rgb(30,87,134);
        border-width: 1px;
        margin: 0px 10px;
        height: 0;
    }
    a {
        text-decoration: none;
        color: rgb(30,87,134);
    }
</style>