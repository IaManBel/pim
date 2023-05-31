import itk
import argparse
import sys
import numpy as np

# Step 1 Pipeline - RGB to Grayscale Conversion

parser = argparse.ArgumentParser(description="Compute RGB Image To Grayscale Image and Perform Median Filtering.")
parser.add_argument("input_image")
parser.add_argument("output_image")
args = parser.parse_args()

Dimension = 2

ComponentType = itk.UC
InputPixelType = itk.RGBPixel[ComponentType]
InputImageType = itk.Image[InputPixelType, Dimension]

OutputPixelType = itk.UC
OutputImageType = itk.Image[OutputPixelType, Dimension]

reader = itk.ImageFileReader[InputImageType].New()
reader.SetFileName(args.input_image)

rgbFilter = itk.RGBToLuminanceImageFilter.New(reader)

# Step 2 Pipeline - Median Filtering

PixelType = itk.UC
ImageType = itk.Image[PixelType, Dimension]

medianFilter = itk.MedianImageFilter[ImageType, ImageType].New()
medianFilter.SetRadius(1)  # Set radius value to 1 for median filter

# Connect the output of Program 1 to Program 2
medianFilter.SetInput(rgbFilter.GetOutput())

# ImageFileWriter for Program 2
medianOutputFileName = "median_output.png"
writer1 = itk.ImageFileWriter[ImageType].New()
writer1.SetFileName(medianOutputFileName)
writer1.SetInput(medianFilter.GetOutput())

writer1.Update()


# Step 3 Pipeline - Gradient Magnitude Filtering

InputPixelType3 = itk.UC
InputImageType3 = itk.Image[InputPixelType3, Dimension]

OutputPixelType3 = itk.UC
OutputImageType3 = itk.Image[OutputPixelType3, Dimension]

inputImage3 = itk.imread(medianOutputFileName, InputPixelType3)

# Create and setup a gradient filter
FilterType3 = itk.GradientMagnitudeImageFilter[InputImageType3, OutputImageType3]
gradientFilter = FilterType3.New()
gradientFilter.SetInput(inputImage3)

# ImageFileWriter for Program 3
gradientOutputFileName = args.output_image  # Use the value from the command-line argument
try:
    itk.imwrite(gradientFilter.GetOutput(), gradientOutputFileName)
except Exception as error:
    print("Error:", error)
    sys.exit(1)


# Step 4 Pipeline - Mean Filtering

PixelType4 = itk.UC
Dimension4 = 2

ImageType4 = itk.Image[PixelType4, Dimension4]

reader4 = itk.ImageFileReader[ImageType4].New()
reader4.SetFileName(gradientOutputFileName)

meanFilter = itk.MeanImageFilter[ImageType4, ImageType4].New()
meanFilter.SetInput(reader4.GetOutput())
meanFilter.SetRadius(2)  # Set radius value to 1 for mean filter

writer4 = itk.ImageFileWriter[ImageType4].New()
meanOutputFileName = gradientOutputFileName  # Use the value from the command-line argument
writer4.SetFileName(meanOutputFileName)
writer4.SetInput(meanFilter.GetOutput())

writer4.Update()


# Step 5 Pipeline - Curvature Flow

InputPixelType5 = itk.F
OutputPixelType5 = itk.UC
Dimension5 = 2

InputImageType5 = itk.Image[InputPixelType5, Dimension5]
OutputImageType5 = itk.Image[OutputPixelType5, Dimension5]

reader5 = itk.ImageFileReader[InputImageType5].New()
reader5.SetFileName(meanOutputFileName)

curvatureFlowFilter = itk.CurvatureFlowImageFilter[InputImageType5, InputImageType5].New()
curvatureFlowFilter.SetInput(reader5.GetOutput())
curvatureFlowFilter.SetNumberOfIterations(1)  # Set number of iterations to 1
curvatureFlowFilter.SetTimeStep(2.0)  # Set time step to 2.0

rescaler5 = itk.RescaleIntensityImageFilter[InputImageType5, OutputImageType5].New()
rescaler5.SetInput(curvatureFlowFilter.GetOutput())

outputPixelTypeMinimum5 = itk.NumericTraits[OutputPixelType5].min()
outputPixelTypeMaximum5 = itk.NumericTraits[OutputPixelType5].max()

rescaler5.SetOutputMinimum(outputPixelTypeMinimum5)
rescaler5.SetOutputMaximum(outputPixelTypeMaximum5)

writer5 = itk.ImageFileWriter[OutputImageType5].New()
writer5.SetFileName(args.output_image)
writer5.SetInput(rescaler5.GetOutput())

# Execute the pipeline of Program 5
writer5.Update()


# Step 6 Pipeline - Maximum Value Kernel Processing

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

# Get the input image file name from the command line argument
input_image_file = args.output_image

# Get the output image file name from the command line argument
output_image_file = "output_program6.png"

# Specify the size of the kernel
kernel_size = 3

# Load the input image
InputImageType6 = itk.Image[itk.UC, 2]
reader6 = itk.ImageFileReader[InputImageType6].New()
reader6.SetFileName(input_image_file)
reader6.Update()

input_image6 = reader6.GetOutput()

# Create the kernel with maximum value
kernel6 = create_max_value_kernel(kernel_size)

# Perform image padding
pad_filter6 = itk.ConstantPadImageFilter[InputImageType6, InputImageType6].New()
pad_filter6.SetInput(input_image6)
pad_filter6.SetConstant(0)  # Set the padding value
pad_filter6.SetPadLowerBound([kernel_size // 2, kernel_size // 2])
pad_filter6.SetPadUpperBound([kernel_size // 2, kernel_size // 2])
pad_filter6.Update()

padded_image6 = pad_filter6.GetOutput()

# Perform image processing by assigning the maximum value in the kernel to each pixel
output_image6 = itk.Image[itk.UC, 2].New()
output_image6.SetRegions(input_image6.GetLargestPossibleRegion())
output_image6.CopyInformation(input_image6)
output_image6.Allocate()

output_image_pixels6 = itk.GetArrayViewFromImage(output_image6)
padded_image_pixels6 = itk.GetArrayViewFromImage(padded_image6)

for y in range(input_image6.GetLargestPossibleRegion().GetSize()[1]):
    for x in range(input_image6.GetLargestPossibleRegion().GetSize()[0]):
        region6 = itk.ImageRegion[2]()
        region6.SetSize([kernel_size, kernel_size])
        region6.SetIndex([x, y])

        kernel_pixels6 = padded_image_pixels6[region6.GetIndex()[1]:region6.GetIndex()[1] + region6.GetSize()[1],
                                            region6.GetIndex()[0]:region6.GetIndex()[0] + region6.GetSize()[0]]
        highest_value6 = np.max(kernel_pixels6)
        
        output_image_pixels6[y, x] = highest_value6

# Save the processed image to the output file
itk.imwrite(output_image6, output_image_file)

print("Processing completed!")

