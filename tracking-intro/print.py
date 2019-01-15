import DataFormats.FWLite as fwlite
events = fwlite.Events("tracks_and_vertices.root")
tracks = fwlite.Handle("std::vector<reco::Track>")
MVAs   = fwlite.Handle("std::vector<float>")

printTracks_1 = False
printTracks_2 = True
nEvents = 1

# print tracks v1
if printTracks_1:
    for i, event in enumerate(events):
        if i >= nEvents: break            # only the first 5 events
        print "Event", i
        event.getByLabel("generalTracks", tracks)
        for j, track in enumerate(tracks.product()):
            print "    Track", j, track.charge()/track.pt(), track.phi(), track.eta(), track.dxy(), track.dz()

# print tracks v2
if printTracks_2:
    for i, event in enumerate(events):
        if i >= nEvents: break            # only the first 5 events
        print "Event", i
        event.getByLabel("generalTracks", tracks)
        event.getByLabel("generalTracks", "MVAValues", MVAs)
    
        numTotal = tracks.product().size()
        numLoose = 0
        numTight = 0
        numHighPurity = 0
    
        for j, (track, mva) in enumerate(zip(tracks.product(), MVAs.product())):
            if track.quality(track.qualityByName("loose")):      numLoose      += 1
            if track.quality(track.qualityByName("tight")):      numTight      += 1
            if track.quality(track.qualityByName("highPurity")): numHighPurity += 1
    
            print "    Track", j,
            print track.charge()/track.pt(),
            print track.phi(),
            print track.eta(),
            print track.dxy(),
            print track.dz(),
            print track.numberOfValidHits(),
            print track.algoName(),
            print mva
    
        print "Event", i,
        print "numTotal:", numTotal,
        print "numLoose:", numLoose,
        print "numTight:", numTight,
        print "numHighPurity:", numHighPurity
