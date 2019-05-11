/**
 * Created by montanawong on 5/10/19.
 */


function scrape() {
    var solos = true;
    //solos
    var colToType = {
        0: "rank",
        1:  "name",
        2: "points",
        3: "prize"
    };
    var slicks = $(".slick-track");

    var slickSlides = slicks[1].children;

    var standings = [];

    for (var i = 0; i < slickSlides.length; i++) {
        var rows = slickSlides[i].childNodes[0].children[1].children;
        for (var j = 0; j < rows.length; j++) {
            var row = rows[j];
            var cols = row.childNodes;
            var standing = {};
            for (var k = 0; k < cols.length; k++) {
                var col = cols[k];
                var content = col.textContent;
                if (solos) {
                    if (k === 2) {
                        content = Number(content);
                    } else if (k === 3) {
                        content = Number(content.slice(2));
                    }
                }
                standing[colToType[k]] = content
            }
            standings.push(standing);
        }
    }
    copy(standings);
    console.log(standings);

}