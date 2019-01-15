import DataFormats.FWLite as fwlite
import ROOT
import math

events = fwlite.Events("tracks_and_vertices.root")
tracks = fwlite.Handle("std::vector<reco::Track>")

printKE = False

# The pion mass is 0.140 GeV (all masses in CMSSW are in GeV). 
pionMass = 0.140

if printKE: 
    for i, event in enumerate(events):
        event.getByLabel("generalTracks", tracks)
        for track in tracks.product():
            # kinetic energy
            # E^2 = p^2c^2 + m^2c^4
            E = math.sqrt( track.p() ** 2 + pionMass ** 2 ) 
            # KE = E - mc^2
            KE = E - pionMass
            print track.pt(), track.p(), track.px(), track.py(), track.pz(),
            print E, KE
        if i > 10: break

px_histogram = ROOT.TH1F("px", "px", 100, -1000.0, 1000.0)
py_histogram = ROOT.TH1F("py", "py", 100, -1000.0, 1000.0)
pz_histogram = ROOT.TH1F("pz", "pz", 100, -1000.0, 1000.0)
E_histogram = ROOT.TH1F("E", "E", 100, -1000.0, 1000.0)
KE_histogram = ROOT.TH1F("KE", "KE", 100, -1000.0, 1000.0)

events.toBegin()                # start event loop from the beginning
for event in events:
    event.getByLabel("generalTracks", tracks)
    total_px = 0.0
    total_py = 0.0
    total_pz = 0.0
    total_E = 0.0
    total_KE = 0.0
    for track in tracks.product():
        # kinetic energy
        # E^2 = p^2c^2 + m^2c^4
        E = math.sqrt( track.p() ** 2 + pionMass ** 2 ) 
        # KE = E - mc^2
        KE = E - pionMass
        total_px += track.px()
        total_py += track.py()
        total_pz += track.pz()
        total_E += E
        total_KE += KE
    px_histogram.Fill(total_px)
    py_histogram.Fill(total_py)
    pz_histogram.Fill(total_pz)
    E_histogram.Fill(total_E)
    KE_histogram.Fill(total_KE)
    # no break statement; we're looping over all events

c = ROOT.TCanvas ("c" , "c", 800, 800)
px_histogram.Draw()
c.SaveAs("track_px.png")
py_histogram.Draw()
c.SaveAs("track_py.png")
pz_histogram.Draw()
c.SaveAs("track_pz.png")
E_histogram.Draw()
c.SaveAs("track_E.png")
KE_histogram.Draw()
c.SaveAs("track_KE.png")

