import DataFormats.FWLite as fwlite
import ROOT
import math

events = fwlite.Events("tracks_and_vertices.root")
tracks = fwlite.Handle("std::vector<reco::Track>")
plotDir = "plots"

# The pion mass is 0.106 GeV (all masses in CMSSW are in GeV). 
muonMass = 0.106

Minv_histogram = ROOT.TH1F("Minv", "Minv", 100, 0.0, 5.0)

events.toBegin()                # start event loop from the beginning
for i_event, event in enumerate(events):
    # no break statement for testing, remove for final plots
    #if i_event >= 100: break
    #event.getByLabel("generalTracks", tracks)
    event.getByLabel("globalMuons", tracks)
    n_tracks = len(tracks.product())
    # exclude events that do not have exactly two muons
    if n_tracks != 2:
        #print "i_event = {0} n_tracks = {1}".format(i_event, n_tracks)
        continue
    # loop over tracks
    for i in xrange(n_tracks):
        # loop over tracks again (without double counting) to get pairs of tracks
        for j in xrange(i+1, n_tracks): 
            track1 = tracks.product()[i]
            track2 = tracks.product()[j]
            # 4-vector addition: p_total = p1 + p2
            # E = E1 + E2, p_i = p1_i + p2_i
            total_energy = math.sqrt(muonMass**2 + track1.p()**2) + math.sqrt(muonMass**2 + track2.p()**2)
            total_px = track1.px() + track2.px()
            total_py = track1.py() + track2.py()
            total_pz = track1.pz() + track2.pz()
            Minv = math.sqrt(total_energy**2 - total_px**2 - total_py**2 - total_pz**2)
            Minv_histogram.Fill(Minv)

c = ROOT.TCanvas ("c" , "c", 800, 800)
Minv_histogram.Draw()
c.SetLogy()
c.SaveAs(plotDir + "/" + "track_Minv.png")

