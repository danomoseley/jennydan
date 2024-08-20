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
      img.addEventListener('click', function() {
        const getPresignedDeleteUrlResponse = fetch('/photos', {
          method: 'DELETE',
          headers: {
            'Content-Type': 'application/json'
          },
          body: JSON.stringify({
            objectKey: objectKey,
            fileType: file.type
          })
        });

        if (!getPresignedDeleteUrlResponse.ok) {
          console.error('Failed to get presigned delete URL');
        }

        const { presignedDeleteUrl, objectKey } = getPresignedDeleteUrlResponse.json();

        const deleteFromR2Response = await fetch(presignedDeleteUrl, {
          method: 'DELETE'
        });

        if (!deleteFromR2Response.ok) {
          console.error('Failed to delete file from R2');
        }

        img.style.display="none"
      });
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

<div id="photos">
  <h2>Share Your Photos!</h2>
  <p style="margin-bottom:20px;">When your photos have uploaded successfully they will display below. Do not leave the page until all photos have finished uploading and the loading indicator stops. If you refresh the page the photos will disappear, but don't worry we will still have them! Feel free to upload as many as you'd like.</p>
  <Fileupload id="multiple_files" multiple bind:files on:change={handleFileUpload} />
  <div id="spinner" style="display:none; margin:10px;"><Spinner size={20} /></div>
  <div id="uploaded_images"></div>
</div>