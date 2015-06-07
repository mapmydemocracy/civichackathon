'use strict';

angular.module('clientApp')
  .factory('jurisdictions', function () {
    var o = 
    {
      jurisdictions: [
        {
          name: 'San Francisco',
          offices : [
            {
              name: "Mayor",
              districts: []
            },
            {
              name: "Supervisor",
              districts: [
                { name: "District 3",
                  contests: [
                    {
                      name: new Date('2015', '11', '05').toString(),
                      candidates: [
                        {name: "Julie Christensen"},
                        {name: "Aaron Peskin"}
                      ]
                    },
                    {
                     name: new Date('2016', '11', '05').toString(),
                      candidates: []
                    }
                  ]
              },
              {name: "District 4"},
              {name: "District 5"},
              {name: "District 7"},
              {name: "District 11"}

              ]
            },

            {name : "City Attorney"}
          ]
        },
        {
          name : 'BART',
          districts : [] 
        },
        {
          name : 'San Francisco Unified School District',
          districts : [] 
        },
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
      var jurisdiction_offices = o.parseObjArray(o.jurisdictions, jurisdiction).offices;

      console.log(jurisdiction_offices.offices)

      // var office_districts = o.parseObjArray(jurisdiction_offices, district);

      jurisdiction_offices.push({name:district, contests:[]})

      console.log('Adding district ', district)
    }

    o.addContest = function(jurisdiction, office, district, contest){
      // o.jurisdictions[jurisdiction][office][district]['contests'].push({date: contest, candidates:[]})

/*      var jurisdiction_offices = parseObjArray(o.jurisdictions, office);

      var office_districts = parseObjArray(jurisdiction_offices, district);

      var district_contests = parseObjArray(office_districts)

      district_contests.push(contest)*/


      console.log('Adding contest ', contest)
    }

    o.addCandidate = function(jurisdiction, office, district, contest, candidate){
      // o.jurisdictions.jurisdiction.office.district.contest['candidates'].push({name: contest, candidates:[]})

/*      var jurisdiction_offices = parseObjArray(o.jurisdictions, office);

      var office_districts = parseObjArray(jurisdiction_offices, district);

      var district_contests = parseObjArray(office_districts)*/

      // var contest_candidates = parseObjArray(district_contests, candidates)
      console.log('Adding candidate ', candidate)
    }


    return o

  });
