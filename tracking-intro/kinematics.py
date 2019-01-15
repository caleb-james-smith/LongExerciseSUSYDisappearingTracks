import DataFormats.FWLite as fwlite
import ROOT

events = fwlite.Events("tracks_and_vertices.root")
tracks = fwlite.Handle("std::vector<reco::Track>")

for i, event in enumerate(events):
    event.getByLabel("generalTracks", tracks)
    for track in tracks.product():
        print track.pt(), track.p(), track.px(), track.py(), track.pz()
    if i > 100: break
