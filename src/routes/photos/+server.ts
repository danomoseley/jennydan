import { PUBLIC_S3_BUCKET_NAME } from '$env/static/public';
import { PutObjectCommand } from '@aws-sdk/client-s3';
import { getSignedUrl } from '@aws-sdk/s3-request-presigner';
import { json } from "@sveltejs/kit";

import { R2_ACCESS_KEY, R2_ACCOUNT_ID, R2_SECRET_KEY } from "$env/static/private";
import { S3Client } from "@aws-sdk/client-s3";

const S3 = new S3Client({
    region: "auto",
    endpoint: `https://${R2_ACCOUNT_ID}.r2.cloudflarestorage.com`,
    credentials: {
        accessKeyId: R2_ACCESS_KEY,
        secretAccessKey: R2_SECRET_KEY,
    },
});

const slugifyString = (str: string) => {
    return str.trim().toLowerCase().replace(/\s+/g, '-').replace(/\./g, '-').replace(/-+/g, '-').replace(/[^a-z0-9-]/g, '-');
}

export async function POST({ request, cookies }) {
    const { fileName, fileType, } = await request.json() as { fileName: string | undefined, fileType: string | undefined };

    if (!fileName || !fileType || fileName.trim() === '' || fileType.trim() === '') {
        return json({ message: 'Missing required parameters.' }, { status: 400 });
    }

    const objectKey = `${slugifyString(Date.now().toString())}-${slugifyString(fileName)}`;

    const presignedUrl = await getSignedUrl(S3, new PutObjectCommand({
        Bucket: PUBLIC_S3_BUCKET_NAME,
        Key: objectKey,
        ContentType: fileType,
        ACL: 'public-read'
    }), {
        expiresIn: 60 * 5 // 5 minutes
    });

    return json({ presignedUrl, objectKey });
}

export async function DELETE({ request, cookies }) {
    const { objectKey, fileType, } = await request.json() as { objectKey: string | undefined, fileType: string | undefined };

    if (!objectKey || !fileType || objectKey.trim() === '' || fileType.trim() === '') {
        return json({ message: 'Missing required parameters.' }, { status: 400 });
    }

    const presignedUrl = await getSignedUrl(S3, new DeleteObjectCommand({
        Bucket: PUBLIC_S3_BUCKET_NAME,
        Key: objectKey,
        ContentType: fileType,
        ACL: 'public-read'
    }), {
        expiresIn: 60 * 5 // 5 minutes
    });

    return json({ presignedUrl, objectKey });
}
