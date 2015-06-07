'use strict';

angular.module('clientApp')
  .factory('jurisdictions', function () {
    var o = 
    {
      jurisdictions: [
        {
          name: 'jurisdiction_one',
          offices : [
            {
              name: "Mayor",
              districts: []
            },
            {
              name: "Supervisor",
              districts: [
                {name: "District 1"},
                {name: "District 2"}
              ]
            }
          ]
        }
      ]
        
    }

    o.parseObjArray = function(objectsArray, name) {
      for (var i in objectsArray) {
        if (objectsArray[i].name == name) return objectsArray[i]
      }
    }
    

    o.addJurisdiction = function(jurisdiction) {
        o.jurisdictions.push({name:jurisdiction, districts:[]})
        console.log('Adding jurisdiction ', jurisdiction)
      }

    o.addOffice = function(jurisdiction, office) {

      var jurisdiction_offices = o.parseObjArray(o.jurisdictions, jurisdiction);
      console.log(jurisdiction_offices)
      jurisdiction_offices['offices'].push({name:office, districts:[]})
      console.log(jurisdiction_offices)
      console.log('Adding office ', office)
    }

    o.addDistrict = function(jurisdiction, office, district){
      // o.jurisdictions[jurisdiction][office]['districts'].push({name: district, contests:[]})
      
      // var jurisdiction_offices = o.parseObjArray(o.jurisdictions, office);

      // var office_districts = parseObjArray(jurisdiction_offices, district);

      // office_districts.push(district)

      console.log('Adding district ', district)
    }

    // o.addContest = function(jurisdiction, office, district, contest){
    //   // o.jurisdictions[jurisdiction][office][district]['contests'].push({date: contest, candidates:[]})

    //   var jurisdiction_offices = parseObjArray(o.jurisdictions, office);

    //   var office_districts = parseObjArray(jurisdiction_offices, district);

    //   var district_contests = parseObjArray(office_districts)

    //   district_contests.push(contest)


    //   contests.log('Adding contest ', district)
    // }

    // o.addCandidate = function(jurisdiction, office, district, contest, candidates){
    //   // o.jurisdictions.jurisdiction.office.district.contest['candidates'].push({name: contest, candidates:[]})

    //   var jurisdiction_offices = parseObjArray(o.jurisdictions, office);

    //   var office_districts = parseObjArray(jurisdiction_offices, district);

    //   var district_contests = parseObjArray(office_districts)

    //   // var contest_candidates = parseObjArray(district_contests, candidates)
    //   contests.log('Adding contest ', district)
    // }


    return o

  });
