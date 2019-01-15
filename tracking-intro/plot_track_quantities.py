import DataFormats.FWLite as fwlite
import ROOT

events = fwlite.Events("tracks_and_vertices.root")
tracks = fwlite.Handle("std::vector<reco::Track>")

hist_pt   = ROOT.TH1F("pt", "pt", 100, 0.0, 100.0)
hist_eta  = ROOT.TH1F("eta", "eta", 100, -3.0, 3.0)
hist_phi  = ROOT.TH1F("phi", "phi", 100, -3.2, 3.2)
hist_normChi2 = ROOT.TH1F("normChi2", "normChi2", 100, 0.0, 10.0)

for i, event in enumerate(events):
    event.getByLabel("generalTracks", tracks)
    for track in tracks.product():
        hist_pt.Fill(track.pt())
        hist_eta.Fill(track.eta())
        hist_phi.Fill(track.phi())
        hist_normChi2.Fill(track.normalizedChi2())
    if i > 1000: break

c = ROOT.TCanvas( "c", "c", 800, 800)

hist_pt.Draw()
c.SetLogy()
c.SaveAs("track_pt.png")
c.SetLogy(False)

hist_eta.Draw()
c.SaveAs("track_eta.png")

hist_phi.Draw()
c.SaveAs("track_phi.png")

hist_normChi2.Draw()
c.SaveAs("track_normChi2.png")
