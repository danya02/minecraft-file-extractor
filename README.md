# Minecraft asset extractor
The Minecraft asset extractor is a program that takes a `.minecraft` folder and
extracts whatever asset files it finds therein to a folder of your choosing.
Here's how it works:

## Executed actions
(For this description, `$IN` means the `.minecraft` folder from which to take the
input and `$OUT` means the folder to write the output to.)

1. The program changes directory to `$IN/assets/indexes` and gets the file
names (those are of type `$(version number).json`) and, if there are multiple,
prompts the user to select one.

2. The program reads the selected file and, for each object under the `objects`
key, does action 3, and does action 4 afterwards.

3. The program changes directory to `$IN/assets/objects/$(hash[0:2])`, reads the
file `$(hash)` and writes it out to the corresponding directory under `$OUT`.

4. The program prints the information on the operation.
