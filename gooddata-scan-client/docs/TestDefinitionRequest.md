# TestDefinitionRequest

A request containing all information for testing data source definition.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Type of database, where test should connect to. | 
**url** | **str** | URL to database in JDBC format, where test should connect to. | 
**schema** | **str** | Database schema. | [optional] 
**username** | **str** | Database user name. | [optional] 
**password** | **str** | Database user password. | [optional] 
**token** | **str** | Secret for token based authentication for data sources which supports it. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


