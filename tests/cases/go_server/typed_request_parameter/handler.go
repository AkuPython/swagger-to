// Code generated by swagger_to. DO NOT EDIT.
package product

// Automatically generated file by swagger_to. DO NOT EDIT OR APPEND ANYTHING!

import "net/http"

// Handler defines an interface to handling the routes.
type Handler interface {
	// TestEndpoint handles the path `/test_endpoint` with the method "get".
	//
	// Path description:
	// test typed request parameter
	TestEndpoint(w http.ResponseWriter,
		r *http.Request,
		stringParam string,
		stringOptionalParam *string,
		int32Param *int32,
		int64Param *int64,
		floatParam *float32,
		booleanParam *bool)
}

// Automatically generated file by swagger_to. DO NOT EDIT OR APPEND ANYTHING!
