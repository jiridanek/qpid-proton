/*
 *
 * Licensed to the Apache Software Foundation (ASF) under one
 * or more contributor license agreements.  See the NOTICE file
 * distributed with this work for additional information
 * regarding copyright ownership.  The ASF licenses this file
 * to you under the Apache License, Version 2.0 (the
 * "License"); you may not use this file except in compliance
 * with the License.  You may obtain a copy of the License at
 *
 *   http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing,
 * software distributed under the License is distributed on an
 * "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
 * KIND, either express or implied.  See the License for the
 * specific language governing permissions and limitations
 * under the License.
 *
 */

#ifndef _LIB_FUZZING_ENGINE_H_
#define _LIB_FUZZING_ENGINE_H_

#include <stdint.h>
#include <stdlib.h>

#include <proton/import_export.h>

// This header defines `extern "C"` for the fuzzing interface functions
//  and exports the functions so that honggfuzz will not override them with weak symbol stand-ins

#ifdef __cplusplus
extern "C"
#endif
PN_EXPORT int LLVMFuzzerInitialize(int *argc, char ***argv);

#ifdef __cplusplus
extern "C"
#endif
PN_EXPORT int LLVMFuzzerTestOneInput(uint8_t *Data, size_t Size);

#endif
