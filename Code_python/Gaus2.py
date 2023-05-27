import itk
import sys

# Verify command line arguments
if len(sys.argv) != 3:
    print("Usage: ")
    print(sys.argv[0] + " <InputImage> <OutputImage>")
    sys.exit(1)

inputFileName = sys.argv[1]
outputFileName = sys.argv[2]

Dimension = 2

InputPixelType = itk.UC
InputImageType = itk.Image[InputPixelType, Dimension]

OutputPixelType = itk.UC
OutputImageType = itk.Image[OutputPixelType, Dimension]

inputImage = itk.imread(inputFileName, InputPixelType)

# Create and setup a gradient filter
FilterType = itk.GradientMagnitudeImageFilter[InputImageType, OutputImageType]
gradientFilter = FilterType.New()
gradientFilter.SetInput(inputImage)

try:
    itk.imwrite(gradientFilter.GetOutput(), outputFileName)
except Exception as error:
    print("Error:", error)
    sys.exit(1)

