import DataFormats.FWLite as fwlite
import ROOT
import math

events = fwlite.Events("tracks_and_vertices.root")
tracks = fwlite.Handle("std::vector<reco::Track>")
# The pion mass is 0.140 GeV (all masses in CMSSW are in GeV). 
pionMass = 0.140

for i, event in enumerate(events):
    event.getByLabel("generalTracks", tracks)
    for track in tracks.product():
        # kinetic energy
        # KE = p^2 / (2m)
        #kineticEnergy = ( track.p() ** 2 ) / ( 2 * pionMass )
        # E^2 = p^2c^2 + m^2c^4
        E = math.sqrt( track.p() ** 2 + pionMass ** 2 ) 
        # KE = E - mc^2
        KE = E - pionMass
        print track.pt(), track.p(), track.px(), track.py(), track.pz(),
        print E, KE
    if i > 10: break
