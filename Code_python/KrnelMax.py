import itk
import sys
import numpy as np

def create_max_value_kernel(kernel_size):
    # Define the pixel type and dimension of the kernel
    PixelType = itk.UC
    Dimension = 2

    # Create an ITK image of the specified size and pixel type
    ImageType = itk.Image[PixelType, Dimension]
    kernel = ImageType.New()
    kernel.SetRegions([kernel_size, kernel_size])
    kernel.Allocate()

    return kernel

if len(sys.argv) != 3:
    print("Usage: ", sys.argv[0], "<InputImage> <OutputImage>")
    sys.exit()

# Get the input image file name from the command line argument
input_image_file = sys.argv[1]

# Get the output image file name from the command line argument
output_image_file = sys.argv[2]

# Specify the size of the kernel
kernel_size = 3

# Load the input image
InputImageType = itk.Image[itk.UC, 2]
reader = itk.ImageFileReader[InputImageType].New()
reader.SetFileName(input_image_file)
reader.Update()

input_image = reader.GetOutput()

# Create the kernel with maximum value
kernel = create_max_value_kernel(kernel_size)

# Perform image padding
pad_filter = itk.ConstantPadImageFilter[InputImageType, InputImageType].New()
pad_filter.SetInput(input_image)
pad_filter.SetConstant(0)  # Set the padding value
pad_filter.SetPadLowerBound([kernel_size // 2, kernel_size // 2])
pad_filter.SetPadUpperBound([kernel_size // 2, kernel_size // 2])
pad_filter.Update()

padded_image = pad_filter.GetOutput()

# Perform image processing by assigning the maximum value in the kernel to each pixel
output_image = itk.Image[itk.UC, 2].New()
output_image.SetRegions(input_image.GetLargestPossibleRegion())
output_image.CopyInformation(input_image)
output_image.Allocate()

output_image_pixels = itk.GetArrayViewFromImage(output_image)
padded_image_pixels = itk.GetArrayViewFromImage(padded_image)

for y in range(input_image.GetLargestPossibleRegion().GetSize()[1]):
    for x in range(input_image.GetLargestPossibleRegion().GetSize()[0]):
        region = itk.ImageRegion[2]()
        region.SetSize([kernel_size, kernel_size])
        region.SetIndex([x, y])

        kernel_pixels = padded_image_pixels[region.GetIndex()[1]:region.GetIndex()[1] + region.GetSize()[1],
                                            region.GetIndex()[0]:region.GetIndex()[0] + region.GetSize()[0]]
        highest_value = np.max(kernel_pixels)
        
        output_image_pixels[y, x] = highest_value

# Save the processed image to the output file
itk.imwrite(output_image, output_image_file)

print("Processing completed!")

