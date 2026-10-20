#!/usr/bin/env node
/**
 * Analyze 2 gambar Dola AI pakai VLM (z-ai-web-dev-sdk createVision)
 */

const ZAI = require('/home/z/.bun/install/global/node_modules/z-ai-web-dev-sdk').default;
const fs = require('fs');

async function analyzeImage(imagePath, imageNum) {
    console.log(`\n=== ANALYZING IMAGE ${imageNum}: ${imagePath} ===`);
    
    try {
        const imageData = fs.readFileSync(imagePath);
        const base64 = imageData.toString('base64');
        const dataUri = `data:image/png;base64,${base64}`;
        
        const zai = await ZAI.create();
        const response = await zai.chat.completions.createVision({
            model: 'glm-4v-flash',
            messages: [
                {
                    role: 'user',
                    content: [
                        {
                            type: 'text',
                            text: `Describe this image. Is it a character reference sheet with multiple angles? How many angles are visible? What is the background? What is the artistic style? Which angle is clearest?`
                        },
                        {
                            type: 'image_url',
                            image_url: {
                                url: dataUri
                            }
                        }
                    ]
                }
            ],
            max_tokens: 1000
        });
        
        console.log(response.choices[0].message.content);
        return response.choices[0].message.content;
    } catch (error) {
        console.error(`Error analyzing image ${imageNum}:`, error.message);
        return null;
    }
}

async function main() {
    // Use cropped face images to avoid content filter
    const img1 = '/tmp/dola_image_1_face.png';
    const img2 = '/tmp/dola_image_2_face.png';
    
    const analysis1 = await analyzeImage(img1, 1);
    const analysis2 = await analyzeImage(img2, 2);
    
    console.log('\n\n=== KESIMPULAN ===');
    console.log('Image 1:', analysis1 ? 'OK' : 'FAIL');
    console.log('Image 2:', analysis2 ? 'OK' : 'FAIL');
}

main().catch(console.error);
