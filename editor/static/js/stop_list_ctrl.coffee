'use strict'

class StopListCtrl
  @$inject: ['$scope', 'Stops']
  constructor: (@$scope, @Stops) ->
    # console.log(@$scope)
    @stops = [{name: "Stop 1"}
              {name: "Stop 2"}]

angular.module('TransiteApp').controller 'StopListCtrl', StopListCtrl
