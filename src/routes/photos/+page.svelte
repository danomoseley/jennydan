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

      let span = document.createElement('span')
      span.style.display="block"
      span.style.position="relative"
      span.style.width="100px"
      let img = new Image()
      img.src="https://photos.jennydan.com/"+objectKey

      img.style.display="inline"
      img.style.margin="20px"
      img.width=100

      let svg = document.createElementNS("http://www.w3.org/2000/svg", "svg");
      svg.setAttribute('class', 'w-[48px] h-[48px] text-gray-800 dark:text-white')
      svg.setAttribute('aria-hidden', 'true')
      svg.setAttribute('width', '24')
      svg.setAttribute('height', '24')
      svg.setAttribute('fill', 'currentColor')
      svg.setAttribute('viewBox', '0 0 24 24')
      let path1 = document.createElementNS("http://www.w3.org/2000/svg", 'path');
      path1.setAttribute('fill-rule', 'evenodd')
      path1.setAttribute('clip-rule', 'evenodd')
      path1.setAttribute('d', 'M2 12C2 6.477 6.477 2 12 2s10 4.477 10 10-4.477 10-10 10S2 17.523 2 12Zm7.707-3.707a1 1 0 0 0-1.414 1.414L10.586 12l-2.293 2.293a1 1 0 1 0 1.414 1.414L12 13.414l2.293 2.293a1 1 0 0 0 1.414-1.414L13.414 12l2.293-2.293a1 1 0 0 0-1.414-1.414L12 10.586 9.707 8.293Z');
      svg.appendChild(path1)
      svg.style.position="absolute"
      svg.style.top="-10px"
      svg.style.right="-10px"

      svg.addEventListener('click', () => {
        fetch('/photos', {
          method: 'DELETE',
          headers: {
            'Content-Type': 'application/json'
          },
          body: JSON.stringify({
            objectKey: objectKey,
            fileType: file.type
          })
        }).then(response => {
          if (!response.ok) {
            console.error('Failed to get presigned delete URL');
          }
          return response.json();
        }).then(data => {
          const presignedDeleteUrl = data['presignedUrl']
          fetch(presignedDeleteUrl, {
            method: 'DELETE'
          }).then(response2 => {
            if (!response2.ok) {
              console.error('Failed to delete file from R2');
            }
            img.style.display="none"
          })
        })
      });

      span.appendChild(img)
      span.appendChild(svg)
      document.getElementById("uploaded_images").prepend(span);
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
  <p style="margin-bottom:20px;">When your photos have uploaded successfully they will display below. Click on a photo to delete it.</p>
  <p style="margin-bottom:20px">Do not leave the page until all photos have finished uploading and the loading indicator stops. If you refresh the page the photos will disappear, but don't worry we will still have them! Feel free to upload as many as you'd like.</p>
  <Fileupload id="multiple_files" multiple bind:files on:change={handleFileUpload} />
  <div id="spinner" style="display:none; margin:10px;"><Spinner size={20} /></div>
  <div id="uploaded_images"></div>
</div>