cmsdas2018/tools/EstimateBackground/PropmtBkg

step 1: Prepare histograms using TagNProbe_histProducer.py . The scripts prepares histograms for kappa calculation, from Gen Information and Tag and Probe method.
Input for the script:
a) Drell Yann MC files (in case of Tag and Probe method) or any MC sample in case of Kappa calculation from Gen Information.
b) Response Templates for smearing which has to be produced from the script ResponseBuilder.py
Output: root file with histograms.
USAGE: python python/SubmitTagProbe_jobs.py python/TagNProbe_histProducer_CutBased.py "INPUT DATA"
 
Step 2: Calculate kappa using Get_kappa.py.
Input for the script: 
a) Root file with histograms obtained from step 1
output: root file with Kappa as a function of eta and Pt.
USAGE: python python/Get_kappa.py <INPUT FILE> <OUTPUT FILE>

Step 3 : Fill closure histograms using script PromptBkgHistMaker.py. Script make histograms of the single lepton control region, predected prompt background and the true background.
Input for the script:
a) W+Jets MC samples 
b) Root file with kappa obtained from step 2
c) Response templates to smear Pt of leptons in the control region 
output: root file with trees.

USAGE: python python/SubmitClosure_jobs.py python/PromptBkgHistMaker.py "INPUT DATA"

Step 4: Plot the closure test histograms using closurePromptBkg.py. Script overlays the control region, predicted bakground, the true background and plots the the ratio between the predicted background and true background.
Input for the script:
a) Root file obtained in step 3
output: Closure Plots

USAGE: python python/closurePromptBkg.py <INPUT FILE>