'use strict'

# class Stops
#   @$inject: ['$resource', '$log']
#   url = "/api/stops/:id"
#   constructor:(@$resource, @$log) ->
#     return $resource url, {id: "@id"}, { update: {method: "PUT"} } 


# angular.module("TransiteApp").factory "Stops", Stops

base_name = 'api.services'

class Stops
  @$inject: ['$http', '$log']
  constructor: (@$log, @$http) ->

  _get: (relPath)->
    return @$http.get("#{@env.serverUrl}/#{relPath}")

  getPeople: () ->
    return @_get('people')

  getPerson: (id) ->
    return @_get("person/#{id}")

angular.module("#{base_name}.stops", []).service "#{base_name}.stops", Stops

