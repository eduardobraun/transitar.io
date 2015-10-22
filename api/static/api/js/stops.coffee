'use strict'

class Stops
  @$inject: ['$resource', '$log']
  url = "/api/stops/:id"
  constructor:(@$resource, @$log) ->
    return $resource url, {id: "@id"}, { update: {method: "PUT"} } 


angular.module("TransiteApp").factory "Stops", Stops

