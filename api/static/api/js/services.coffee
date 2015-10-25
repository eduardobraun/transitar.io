'use strict'

base_name = 'api.services'

apiDataTransformer = ($http) ->
  return $http.defaults.transformResponse.concat([
         (data, headersGetter) ->
           result = data.data
           result.meta = data.meta
           return result])

class Stops
  url = "/api/stops/:id"
  @$inject: ['$log', '$resource', '$http']
  constructor: (@$log, @$resource, @$http) ->
    qry = { method: 'GET', isArray: true, transformResponse: apiDataTransformer(@$http)}
    @_stops = $resource url, {}, { query: qry, update: {method: "PUT"}}

  get: (args) ->
    return @_stops.get(args)

angular.module("#{base_name}.stops", []).service "#{base_name}.stops", Stops

