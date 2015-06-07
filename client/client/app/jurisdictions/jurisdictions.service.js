'use strict';

angular.module('clientApp')
  .factory('jurisdictions', function () {
    var o = 
    {
      jurisdictions: [
        {
          name: 'San Francisco City and County',
          districts : [
            {
              name: "Supervisor District 1"
            },
            {name: "Supervisor District 2"},
            {name: "Supervisor District 3"},
            {name: "Supervisor District 4"}
          ]
        }
      ]
        
    }
    

    o.addJurisdiction = function(j) {
        o.jurisdictions.push({name:j, districts:[]})
        console.log('Adding jurisdiction ', j)
      }

    return o

  });
