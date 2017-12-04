from njmls import get_listings

def test_njmls():
    for listing in get_listings(
            min_beds=4,
            min_baths=2,
            county_search=True,
            counties=['PASSAIC'],
            proptypes=['1']):
        print(listing)
