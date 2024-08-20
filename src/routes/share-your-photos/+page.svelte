<script lang="ts">
  import "../../app.css";
  import { Fileupload, Label, Listgroup, ListgroupItem, Spinner } from 'flowbite-svelte';
  let files; // FileList type
  const handleFileUpload = async (e: Event) => {
    document.getElementById('spinner').style.display='block';
    const target = e.target as HTMLInputElement;

    for (const file of target.files) {
      const getPresignedUrlResponse = await fetch('/share-your-photos', {
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
      span.style.width="140px"
      span.style.float="left"
      let img = new Image()
      if (file.type.startsWith('video')) {
        img.src="/video_icon.png"
      } else {
        img.src="https://photos.jennydan.com/"+objectKey
      }

      img.style.display="inline"
      img.style.margin="20px"
      img.width=100

      let svg = document.createElementNS("http://www.w3.org/2000/svg", "svg");
      svg.setAttribute('class', 'w-[48px] h-[48px] text-gray-800 dark:text-white')
      svg.setAttribute('aria-hidden', 'true')
      svg.setAttribute('width', '24')
      svg.setAttribute('height', '24')
      svg.setAttribute('fill', 'none')
      svg.setAttribute('viewBox', '0 0 24 24')
      let path1 = document.createElementNS("http://www.w3.org/2000/svg", 'path');
      path1.setAttribute('stroke', 'currentColor')
      path1.setAttribute('stroke-linecap', 'round')
      path1.setAttribute('stroke-linejoin', 'round')
      path1.setAttribute('stroke-width', '3')
      path1.setAttribute('d', 'm15 9-6 6m0-6 6 6m6-3a9 9 0 1 1-18 0 9 9 0 0 1 18 0Z');
      svg.appendChild(path1)
      svg.style.position="absolute"
      svg.style.top="0px"
      svg.style.right="0px"

      svg.addEventListener('click', () => {
        fetch('/share-your-photos', {
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
            span.style.display="none"
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
  <p style="margin-bottom:20px;">Thanks for coming to our wedding! Please share your photo memories by uploading them below, so we can experience the weekend over and over.</p>
  <p style="margin-bottom:20px;">When your photos have uploaded successfully they will display below. If you refresh the page the photos will disappear, but don't worry we will still have them!</p>
  <p style="margin-bottom:20px">Do not leave the page until all photos have finished uploading and the loading indicator stops.</p>
  <Fileupload id="multiple_files" multiple bind:files on:change={handleFileUpload} />
  <div id="spinner" style="display:none; margin:10px;"><Spinner size={20} /></div>
  <div id="uploaded_images"></div>
</div>