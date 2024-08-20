<script lang="ts">
  import "../../app.css";
  import { Fileupload, Label, Listgroup, ListgroupItem, Spinner } from 'flowbite-svelte';
  let files; // FileList type
  const handleFileUpload = async (e: Event) => {
    document.getElementById('spinner').style.display='block';
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
      document.getElementById("uploaded_images").prepend(img);
    }
    document.getElementById('spinner').style.display='none';
  };
</script>

<svelte:head>
  <title>Share Your Photos With Us - Jenny & Dan</title>
  <meta name="description" content="Share your wedding day photos with us!" />
</svelte:head>

<main class="max-w-5xl py-12 mx-auto space-y-12">
  <p>Share your photos of our wedding with us by uploading them here!</p>
  <p>When your photos have uploaded successfully they will display below. Do not leave the page until all photos have finished uploading and the loading indicator stops. If you refresh the page the photos will disappear, but don't worry we will still have them! Feel free to upload as many as you'd like.</p>
  <Fileupload id="multiple_files" multiple bind:files on:change={handleFileUpload} />
  <div id="spinner" style="display:none; margin:10px;"><Spinner size={20} /></div>
  <div id="uploaded_images"></div>
</main>