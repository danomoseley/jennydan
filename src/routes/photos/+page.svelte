<script lang="ts">
  import { Fileupload, Label, Listgroup, ListgroupItem } from 'flowbite-svelte';
  let files; // FileList type
  const handleFileUpload = async (e: Event) => {
    const target = e.target as HTMLInputElement;
    const file = target.files?.[0];

    if (file) {
      const getPresignedUrlResponse = await fetch('/photos', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({
          fileName: file.name,
          fileType: file.type
        })
      });

      if (!getPresignedUrlResponse.ok) {
        console.error('Failed to get presigned URL');
      }

      const { presignedUrl, objectKey } = await getPresignedUrlResponse.json();

      const uploadToR2Response = await fetch(presignedUrl, {
        method: 'PUT',
        headers: {
          'Content-Type': file.type
        },
        body: file
      });

      if (!uploadToR2Response.ok) {
        console.error('Failed to upload file to R2');
      }
    }
  };
</script>

<svelte:head>
  <title>Photos - Jenny & Dan</title>
  <meta name="description" content="Share your wedding day photos with us!" />
</svelte:head>

<main class="max-w-5xl py-12 mx-auto space-y-12">
  <Label class="pb-2" for="multiple_files">Upload multiple files</Label>
  <Fileupload id="multiple_files" multiple bind:files on:change={handleFileUpload} />
  <Listgroup items={files} let:item class="mt-2">
    {#if item}
      {item.name}
    {:else}
      <ListgroupItem>No files</ListgroupItem>
    {/if}
  </Listgroup>
</main>