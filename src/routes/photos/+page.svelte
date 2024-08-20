<script lang="ts">
  import "../../app.css";
  import { Fileupload, Label, Listgroup, ListgroupItem, Spinner } from 'flowbite-svelte';
  let files; // FileList type
  const handleFileUpload = async (e: Event) => {
    document.querySelectorAll('.file_spinner').forEach(e => e.style.display='inline');
    const target = e.target as HTMLInputElement;

    for (const file of target.files) {
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

      console.log(objectKey)
      let img = new Image()
      img.src="https://photos.jennydan.com/"+objectKey
      img.style.display="inline"
      img.style.padding="10px"
      img.width=100
      document.getElementById("uploaded_images").appendChild(img);
    }
    document.querySelectorAll('.file_spinner').forEach(e => e.style.display='none');
  };
</script>

<svelte:head>
  <title>Share Your Photos With Us - Jenny & Dan</title>
  <meta name="description" content="Share your wedding day photos with us!" />
</svelte:head>

<main class="max-w-5xl py-12 mx-auto space-y-12">
  <Label class="pb-2" for="multiple_files">Share your photos of our wedding with us by uploading them below!</Label>
  <Fileupload id="multiple_files" multiple bind:files on:change={handleFileUpload} />
  <Listgroup items={files} let:item class="mt-2">
    {#if item}
      {item.name} <span class="file_spinner"><Spinner /></span>
    {:else}
      <ListgroupItem>No files</ListgroupItem>
    {/if}
  </Listgroup>
  <div id="uploaded_images"></div>
</main>