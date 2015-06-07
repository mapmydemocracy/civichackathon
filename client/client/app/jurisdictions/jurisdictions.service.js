'use strict';

angular.module('clientApp')
  .factory('jurisdictions', function () {
    var o = {
      jurisdictions: [
        {name: 'San Francisco City and County'}
      ]
    }

    return {
      info  :  o.jurisdictions,
      add   : function() {
        console.log("hi")
      },


    }

  });
