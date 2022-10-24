#!/bin/bash

ssotme -build

cd ../..
black -l 100 src
cd CodeGenerationTools/GridworksCore/

rm -rf SassyMQ
