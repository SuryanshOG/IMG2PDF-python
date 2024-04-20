import os
import img2pdf

def img2pdfconverter(folder_path):
    if not os.path.exists(folder_path):
        print("Givenj Image folder does not exist")
        return
    images = [imgs for imgs in os.listdir(folder_path) if imgs.endswith(('.jpg', '.jpeg', '.png', '.gif'))]
    
    if not images:
        print("No images found in the given folder")
        return
    images.sort()
    
    images_bytes = []
    
    for i in images:
        try:
            with open(os.path.join(folder_path, i), 'rb') as im:
                images_bytes.append(im.read())
        except Exception as e:
            print(f"Error reading images {i}: {e}")
            
    try:
        pdf_images_bytes = img2pdf.convert(images_bytes)
    except Exception as e:
        print(f"Error convert images to PDF: {e}")
        return
    with open('Output.pdf', "wb") as pdffile:
        pdffile.write(pdf_images_bytes)
        
    print("Images successfully converted to PDF")

if __name__ == "__main__":
    folder_path = input("Enter the path to the images folder: ").strip()
    img2pdfconverter(folder_path)