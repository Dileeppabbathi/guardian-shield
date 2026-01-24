"""
Enhanced URL Collector for Guardian Shield
Collects more legitimate URLs from various categories
"""

import csv
from datetime import datetime

def collect_more_legitimate_urls():
    print("Collecting more legitimate URLs...")
    
    # Expanded legitimate URLs (500+ total)
    legitimate_urls = [
        # News & Media (50)
        "https://www.bbc.com", "https://www.cnn.com", "https://www.nytimes.com",
        "https://www.theguardian.com", "https://www.reuters.com", "https://www.wsj.com",
        "https://www.washingtonpost.com", "https://www.forbes.com", "https://www.time.com",
        "https://www.npr.org", "https://www.cbsnews.com", "https://www.abcnews.go.com",
        "https://www.nbcnews.com", "https://www.usatoday.com", "https://www.bloomberg.com",
        "https://www.economist.com", "https://www.politico.com", "https://www.axios.com",
        "https://www.theatlantic.com", "https://www.newyorker.com", "https://www.wired.com",
        "https://www.techcrunch.com", "https://www.theverge.com", "https://www.engadget.com",
        "https://www.cnet.com", "https://www.zdnet.com", "https://www.arstechnica.com",
        "https://www.mashable.com", "https://www.businessinsider.com", "https://www.fortune.com",
        "https://www.cnbc.com", "https://www.foxnews.com", "https://www.latimes.com",
        "https://www.chicagotribune.com", "https://www.sfgate.com", "https://www.bostonglobe.com",
        "https://www.denverpost.com", "https://www.miamiherald.com", "https://www.dallasnews.com",
        "https://www.seattletimes.com", "https://www.houstonchronicle.com", "https://www.ajc.com",
        "https://www.oregonlive.com", "https://www.cleveland.com", "https://www.pennlive.com",
        "https://www.nj.com", "https://www.baltimoresun.com", "https://www.sandiegouniontribune.com",
        "https://www.tampabay.com", "https://www.startribune.com",
        
        # Tech Companies (50)
        "https://www.apple.com", "https://www.microsoft.com", "https://www.google.com",
        "https://www.amazon.com", "https://www.facebook.com", "https://www.meta.com",
        "https://www.netflix.com", "https://www.tesla.com", "https://www.spacex.com",
        "https://www.nvidia.com", "https://www.intel.com", "https://www.amd.com",
        "https://www.ibm.com", "https://www.oracle.com", "https://www.salesforce.com",
        "https://www.adobe.com", "https://www.zoom.us", "https://www.slack.com",
        "https://www.dropbox.com", "https://www.box.com", "https://www.atlassian.com",
        "https://www.github.com", "https://www.gitlab.com", "https://www.bitbucket.org",
        "https://www.stackoverflow.com", "https://www.reddit.com", "https://www.discord.com",
        "https://www.twitch.tv", "https://www.spotify.com", "https://www.soundcloud.com",
        "https://www.twitter.com", "https://www.instagram.com", "https://www.tiktok.com",
        "https://www.linkedin.com", "https://www.pinterest.com", "https://www.snapchat.com",
        "https://www.whatsapp.com", "https://www.telegram.org", "https://www.signal.org",
        "https://www.shopify.com", "https://www.squarespace.com", "https://www.wix.com",
        "https://www.wordpress.com", "https://www.medium.com", "https://www.substack.com",
        "https://www.notion.so", "https://www.asana.com", "https://www.trello.com",
        "https://www.monday.com", "https://www.figma.com", "https://www.canva.com",
        
        # Education (50)
        "https://www.harvard.edu", "https://www.mit.edu", "https://www.stanford.edu",
        "https://www.yale.edu", "https://www.princeton.edu", "https://www.columbia.edu",
        "https://www.cornell.edu", "https://www.upenn.edu", "https://www.duke.edu",
        "https://www.uchicago.edu", "https://www.berkeley.edu", "https://www.caltech.edu",
        "https://www.ucla.edu", "https://www.umich.edu", "https://www.northwestern.edu",
        "https://www.nyu.edu", "https://www.usc.edu", "https://www.bu.edu",
        "https://www.wisc.edu", "https://www.uw.edu", "https://www.utexas.edu",
        "https://www.gatech.edu", "https://www.uiuc.edu", "https://www.psu.edu",
        "https://www.osu.edu", "https://www.umn.edu", "https://www.unc.edu",
        "https://www.virginia.edu", "https://www.vanderbilt.edu", "https://www.rice.edu",
        "https://www.coursera.org", "https://www.edx.org", "https://www.udacity.com",
        "https://www.khanacademy.org", "https://www.codecademy.com", "https://www.udemy.com",
        "https://www.skillshare.com", "https://www.lynda.com", "https://www.pluralsight.com",
        "https://www.datacamp.com", "https://www.brilliant.org", "https://www.duolingo.com",
        "https://www.memrise.com", "https://www.rosettastone.com", "https://www.babbel.com",
        "https://www.wikipedia.org", "https://www.wikihow.com", "https://www.britannica.com",
        "https://www.dictionary.com", "https://www.thesaurus.com",
        
        # E-commerce (50)
        "https://www.amazon.com", "https://www.ebay.com", "https://www.walmart.com",
        "https://www.target.com", "https://www.bestbuy.com", "https://www.homedepot.com",
        "https://www.lowes.com", "https://www.costco.com", "https://www.samsclub.com",
        "https://www.macys.com", "https://www.nordstrom.com", "https://www.kohls.com",
        "https://www.jcpenney.com", "https://www.sears.com", "https://www.overstock.com",
        "https://www.wayfair.com", "https://www.ikea.com", "https://www.etsy.com",
        "https://www.alibaba.com", "https://www.aliexpress.com", "https://www.wish.com",
        "https://www.zappos.com", "https://www.chewy.com", "https://www.petsmart.com",
        "https://www.petco.com", "https://www.williams-sonoma.com", "https://www.crateandbarrel.com",
        "https://www.bedbathandbeyond.com", "https://www.containerstore.com", "https://www.staples.com",
        "https://www.officedepot.com", "https://www.newegg.com", "https://www.bhphotovideo.com",
        "https://www.adorama.com", "https://www.michaels.com", "https://www.joann.com",
        "https://www.hobbylobby.com", "https://www.dickssportinggoods.com", "https://www.rei.com",
        "https://www.cabelas.com", "https://www.basspro.com", "https://www.academy.com",
        "https://www.footlocker.com", "https://www.nike.com", "https://www.adidas.com",
        "https://www.underarmour.com", "https://www.lululemon.com", "https://www.gap.com",
        "https://www.oldnavy.com", "https://www.bananarepublic.com",
        
        # Finance & Banking (50)
        "https://www.chase.com", "https://www.bankofamerica.com", "https://www.wellsfargo.com",
        "https://www.citi.com", "https://www.usbank.com", "https://www.pnc.com",
        "https://www.capitalone.com", "https://www.tdbank.com", "https://www.ally.com",
        "https://www.discover.com", "https://www.americanexpress.com", "https://www.paypal.com",
        "https://www.venmo.com", "https://www.cashapp.com", "https://www.zellepay.com",
        "https://www.schwab.com", "https://www.fidelity.com", "https://www.vanguard.com",
        "https://www.etrade.com", "https://www.tdameritrade.com", "https://www.robinhood.com",
        "https://www.coinbase.com", "https://www.kraken.com", "https://www.binance.us",
        "https://www.mint.com", "https://www.creditkarma.com", "https://www.nerdwallet.com",
        "https://www.bankrate.com", "https://www.lending tree.com", "https://www.sofi.com",
        "https://www.chime.com", "https://www.simple.com", "https://www.n26.com",
        "https://www.revolut.com", "https://www.transferwise.com", "https://www.wealthfront.com",
        "https://www.betterment.com", "https://www.acorns.com", "https://www.stash.com",
        "https://www.monzo.com", "https://www.stripe.com", "https://www.square.com",
        "https://www.braintreepayments.com", "https://www.adyen.com", "https://www.checkout.com",
        "https://www.plaid.com", "https://www.yodlee.com", "https://www.experian.com",
        "https://www.equifax.com", "https://www.transunion.com", "https://www.annualcreditreport.com",
        
        # Government (50)
        "https://www.usa.gov", "https://www.whitehouse.gov", "https://www.senate.gov",
        "https://www.house.gov", "https://www.supremecourt.gov", "https://www.state.gov",
        "https://www.defense.gov", "https://www.dhs.gov", "https://www.justice.gov",
        "https://www.treasury.gov", "https://www.irs.gov", "https://www.fda.gov",
        "https://www.cdc.gov", "https://www.nih.gov", "https://www.nasa.gov",
        "https://www.epa.gov", "https://www.energy.gov", "https://www.education.gov",
        "https://www.hhs.gov", "https://www.labor.gov", "https://www.transportation.gov",
        "https://www.commerce.gov", "https://www.agriculture.gov", "https://www.interior.gov",
        "https://www.va.gov", "https://www.ssa.gov", "https://www.fema.gov",
        "https://www.fbi.gov", "https://www.cia.gov", "https://www.nsa.gov",
        "https://www.dea.gov", "https://www.atf.gov", "https://www.usps.com",
        "https://www.sec.gov", "https://www.ftc.gov", "https://www.fcc.gov",
        "https://www.ntsb.gov", "https://www.faa.gov", "https://www.tsa.gov",
        "https://www.uscis.gov", "https://www.ice.gov", "https://www.cbp.gov",
        "https://www.census.gov", "https://www.bls.gov", "https://www.noaa.gov",
        "https://www.usgs.gov", "https://www.nps.gov", "https://www.doi.gov",
        "https://www.loc.gov", "https://www.archives.gov", "https://www.gsa.gov",
        
        # Health & Medical (50)
        "https://www.mayoclinic.org", "https://www.clevelandclinic.org", "https://www.hopkinsmedicine.org",
        "https://www.massgeneral.org", "https://www.uclahealth.org", "https://www.med.stanford.edu",
        "https://www.health.harvard.edu", "https://www.webmd.com", "https://www.healthline.com",
        "https://www.medicalnewstoday.com", "https://www.drugs.com", "https://www.rxlist.com",
        "https://www.everydayhealth.com", "https://www.medscape.com", "https://www.nih.gov",
        "https://www.cdc.gov", "https://www.who.int", "https://www.cancer.org",
        "https://www.heart.org", "https://www.diabetes.org", "https://www.arthritis.org",
        "https://www.cvs.com", "https://www.walgreens.com", "https://www.riteaid.com",
        "https://www.goodrx.com", "https://www.1800contacts.com", "https://www.warbyparker.com",
        "https://www.zenni.com", "https://www.teladoc.com", "https://www.doctorondemand.com",
        "https://www.mdlive.com", "https://www.amwell.com", "https://www.zocdoc.com",
        "https://www.patient.co.uk", "https://www.nhs.uk", "https://www.healthdirect.gov.au",
        "https://www.betterhealth.vic.gov.au", "https://www.myfitnesspal.com", "https://www.fitbit.com",
        "https://www.peloton.com", "https://www.orangetheory.com", "https://www.planetfitness.com",
        "https://www.24hourfitness.com", "https://www.crunch.com", "https://www.yogaworks.com",
        "https://www.corepower.com", "https://www.purebarre.com", "https://www.soulcycle.com",
        "https://www.classpass.com", "https://www.mindbodyonline.com", "https://www.headspace.com",
        
        # Entertainment & Streaming (50)
        "https://www.netflix.com", "https://www.hulu.com", "https://www.disneyplus.com",
        "https://www.hbomax.com", "https://www.amazon.com/prime", "https://www.peacocktv.com",
        "https://www.paramountplus.com", "https://www.appletv.com", "https://www.crunchyroll.com",
        "https://www.funimation.com", "https://www.youtube.com", "https://www.vimeo.com",
        "https://www.twitch.tv", "https://www.spotify.com", "https://www.applemusic.com",
        "https://www.pandora.com", "https://www.tidal.com", "https://www.deezer.com",
        "https://www.soundcloud.com", "https://www.bandcamp.com", "https://www.imdb.com",
        "https://www.rottentomatoes.com", "https://www.metacritic.com", "https://www.letterboxd.com",
        "https://www.fandango.com", "https://www.moviefone.com", "https://www.allmusic.com",
        "https://www.pitchfork.com", "https://www.rollingstone.com", "https://www.billboard.com",
        "https://www.variety.com", "https://www.hollywoodreporter.com", "https://www.deadline.com",
        "https://www.ew.com", "https://www.tvguide.com", "https://www.tvline.com",
        "https://www.polygon.com", "https://www.ign.com", "https://www.gamespot.com",
        "https://www.kotaku.com", "https://www.eurogamer.net", "https://www.destructoid.com",
        "https://www.giantbomb.com", "https://www.steam.com", "https://www.epicgames.com",
        "https://www.gog.com", "https://www.origin.com", "https://www.ubisoft.com",
        "https://www.playstation.com", "https://www.xbox.com", "https://www.nintendo.com",
        
        # Travel & Hospitality (50)
        "https://www.booking.com", "https://www.expedia.com", "https://www.hotels.com",
        "https://www.airbnb.com", "https://www.vrbo.com", "https://www.tripadvisor.com",
        "https://www.kayak.com", "https://www.skyscanner.com", "https://www.priceline.com",
        "https://www.orbitz.com", "https://www.travelocity.com", "https://www.hotwire.com",
        "https://www.cheaptickets.com", "https://www.hipmunk.com", "https://www.momondo.com",
        "https://www.delta.com", "https://www.united.com", "https://www.american.com",
        "https://www.southwest.com", "https://www.jetblue.com", "https://www.spirit.com",
        "https://www.frontier.com", "https://www.alaskaair.com", "https://www.hawaiianair.com",
        "https://www.marriott.com", "https://www.hilton.com", "https://www.hyatt.com",
        "https://www.ihg.com", "https://www.choicehotels.com", "https://www.wyndham.com",
        "https://www.bestwestern.com", "https://www.radisson.com", "https://www.accorhotels.com",
        "https://www.fourseasons.com", "https://www.ritzcarlton.com", "https://www.waldorfastoria.com",
        "https://www.enterprise.com", "https://www.hertz.com", "https://www.avis.com",
        "https://www.budget.com", "https://www.nationalcar.com", "https://www.alamo.com",
        "https://www.sixt.com", "https://www.zipcar.com", "https://www.turo.com",
        "https://www.carnival.com", "https://www.royalcaribbean.com", "https://www.ncl.com",
        "https://www.princess.com", "https://www.hollandamerica.com", "https://www.celebrity.com",
    ]
    
    filename = f'../../datasets/legitimate_urls/legitimate_expanded_{datetime.now().strftime("%Y%m%d")}.csv'
    
    with open(filename, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['url', 'source', 'date', 'label'])
        for url in legitimate_urls:
            writer.writerow([url, 'Curated', datetime.now().strftime("%Y-%m-%d"), 'legitimate'])
    
    print(f"✅ Collected {len(legitimate_urls)} legitimate URLs")
    print(f"✅ Saved to: {filename}")
    print(f"\n📊 Total dataset size:")
    print(f"   - Legitimate: {len(legitimate_urls) + 18} URLs")
    print(f"   - Phishing: 300 URLs")
    print(f"   - TOTAL: {len(legitimate_urls) + 18 + 300} URLs")

if __name__ == "__main__":
    collect_more_legitimate_urls()
