import DataFormats.FWLite as fwlite
import ROOT
import math

events = fwlite.Events("tracks_and_vertices.root")
tracks = fwlite.Handle("std::vector<reco::Track>")
plotDir = "plots"

printKE = False

# The pion mass is 0.140 GeV (all masses in CMSSW are in GeV). 
# The pion mass is 0.106 GeV (all masses in CMSSW are in GeV). 
pionMass = 0.140
muonMass = 0.106

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
E_histogram = ROOT.TH1F("E", "E", 100, 0.0, 200.0)
KE_histogram = ROOT.TH1F("KE", "KE", 100, 0.0, 200.0)
Minv_histogram = ROOT.TH1F("Minv", "Minv", 100, 0.0, 200.0)

events.toBegin()                # start event loop from the beginning
for event in events:
    #event.getByLabel("generalTracks", tracks)
    event.getByLabel("globalMuons", tracks)
    sum_px = 0.0
    sum_py = 0.0
    sum_pz = 0.0
    sum_E = 0.0
    sum_KE = 0.0
    for i in xrange(len(tracks.product())):
        track1 = tracks.product()[i]
        # kinetic energy
        # E^2 = p^2c^2 + m^2c^4
        E = math.sqrt( track1.p() ** 2 + muonMass ** 2 ) 
        # KE = E - mc^2
        KE = E - muonMass
        sum_px += track1.px()
        sum_py += track1.py()
        sum_pz += track1.pz()
        sum_E += E
        sum_KE += KE
        # time for track1 pairing
        for j in xrange(len(tracks.product())): 
            track2 = tracks.product()[j]
            # 4-vector addition: p_total = p1 + p2
            # E = E1 + E2, p_i = p1_i + p2_i
            total_energy = math.sqrt(muonMass**2 + track1.p()**2) + math.sqrt(muonMass**2 + track2.p()**2)
            total_px = track1.px() + track2.px()
            total_py = track1.py() + track2.py()
            total_pz = track1.pz() + track2.pz()
            Minv = math.sqrt(total_energy**2 - total_px**2 - total_py**2 - total_pz**2)
            Minv_histogram.Fill(Minv)
    px_histogram.Fill(sum_px)
    py_histogram.Fill(sum_py)
    pz_histogram.Fill(sum_pz)
    E_histogram.Fill(sum_E)
    KE_histogram.Fill(sum_KE)
    # no break statement for testing, remove for final plots
    #if i >= 100: break

c = ROOT.TCanvas ("c" , "c", 800, 800)
px_histogram.Draw()
c.SaveAs(plotDir + "/" + "track_px.png")
py_histogram.Draw()
c.SaveAs(plotDir + "/" + "track_py.png")
pz_histogram.Draw()
c.SaveAs(plotDir + "/" + "track_pz.png")
E_histogram.Draw()
c.SaveAs(plotDir + "/" + "track_E.png")
KE_histogram.Draw()
c.SaveAs(plotDir + "/" + "track_KE.png")
Minv_histogram.Draw()
c.SetLogy()
c.SaveAs(plotDir + "/" + "track_Minv.png")

