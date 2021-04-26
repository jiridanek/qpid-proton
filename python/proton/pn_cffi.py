import cffi

ffi = cffi.FFI()
ffi.set_source(
    module_name='_proton',
    # include_dirs=["/home/jdanek/repos/qpid/qpid-proton/c/include"],
    include_dirs=["/home/jdanek/repos/qpid/qpid-proton/build/install/include"],
    library_dirs=["/home/jdanek/repos/qpid/qpid-proton/build/install/lib64"],
    libraries=["qpid-proton-core"],
    extra_build_args=['-O0'],
    extra_link_args=['-Wl,-rpath=/home/jdanek/repos/qpid/qpid-proton/build/install/lib64'],
    source="""
        //#include "proton/codec.h"
        #include "proton/message.h"
        //typedef struct pn_message_t pn_message_t;
    """,
)
ffi.cdef("""
    typedef struct pn_data_t pn_data_t;

// codec.h

typedef struct pn_atom_t { ...; } pn_atom_t;

// types.h

    typedef uint32_t pn_millis_t;
    typedef struct pn_bytes_t { ...; } pn_bytes_t;
    typedef int64_t pn_timestamp_t;
    typedef uint32_t  pn_sequence_t;
    typedef struct pn_rwbytes_t pn_rwbytes_t;
    typedef struct pn_link_t pn_link_t;

// error.h
    #define PN_OVERFLOW ...
    
    typedef struct pn_error_t pn_error_t;
    
    const char *pn_error_text(pn_error_t *error);

// message.h
    #define PN_DEFAULT_PRIORITY ...

    typedef struct pn_message_t pn_message_t;

pn_message_t * pn_message(void);
void           pn_message_free(pn_message_t *msg);
void           pn_message_clear(pn_message_t *msg);
int            pn_message_errno(pn_message_t *msg);
pn_error_t    *pn_message_error(pn_message_t *msg);
bool           pn_message_is_inferred(pn_message_t *msg);
int            pn_message_set_inferred(pn_message_t *msg, bool inferred);
bool           pn_message_is_durable            (pn_message_t *msg);
int            pn_message_set_durable           (pn_message_t *msg, bool durable);
uint8_t        pn_message_get_priority          (pn_message_t *msg);
int            pn_message_set_priority          (pn_message_t *msg, uint8_t priority);
pn_millis_t    pn_message_get_ttl               (pn_message_t *msg);
int            pn_message_set_ttl               (pn_message_t *msg, pn_millis_t ttl);
bool           pn_message_is_first_acquirer     (pn_message_t *msg);
int            pn_message_set_first_acquirer    (pn_message_t *msg, bool first);
uint32_t       pn_message_get_delivery_count    (pn_message_t *msg);
int            pn_message_set_delivery_count    (pn_message_t *msg, uint32_t count);
pn_data_t *    pn_message_id                    (pn_message_t *msg);
pn_atom_t      pn_message_get_id                (pn_message_t *msg);
int            pn_message_set_id                (pn_message_t *msg, pn_atom_t id);
pn_bytes_t     pn_message_get_user_id           (pn_message_t *msg);
int            pn_message_set_user_id           (pn_message_t *msg, pn_bytes_t user_id);
const char *   pn_message_get_address           (pn_message_t *msg);
int            pn_message_set_address           (pn_message_t *msg, const char *address);
const char *   pn_message_get_subject           (pn_message_t *msg);
int            pn_message_set_subject           (pn_message_t *msg, const char *subject);
const char *   pn_message_get_reply_to          (pn_message_t *msg);
int            pn_message_set_reply_to          (pn_message_t *msg, const char *reply_to);
pn_data_t *    pn_message_correlation_id        (pn_message_t *msg);
pn_atom_t      pn_message_get_correlation_id    (pn_message_t *msg);
int            pn_message_set_correlation_id    (pn_message_t *msg, pn_atom_t id);
const char *   pn_message_get_content_type      (pn_message_t *msg);
int            pn_message_set_content_type      (pn_message_t *msg, const char *type);
const char *   pn_message_get_content_encoding  (pn_message_t *msg);
int            pn_message_set_content_encoding  (pn_message_t *msg, const char *encoding);
pn_timestamp_t pn_message_get_expiry_time       (pn_message_t *msg);
int            pn_message_set_expiry_time       (pn_message_t *msg, pn_timestamp_t time);
pn_timestamp_t pn_message_get_creation_time     (pn_message_t *msg);
int            pn_message_set_creation_time     (pn_message_t *msg, pn_timestamp_t time);
const char *   pn_message_get_group_id          (pn_message_t *msg);
int            pn_message_set_group_id          (pn_message_t *msg, const char *group_id);
pn_sequence_t  pn_message_get_group_sequence    (pn_message_t *msg);
int            pn_message_set_group_sequence    (pn_message_t *msg, pn_sequence_t n);
const char *   pn_message_get_reply_to_group_id (pn_message_t *msg);
int            pn_message_set_reply_to_group_id (pn_message_t *msg, const char *reply_to_group_id);
pn_data_t *pn_message_instructions(pn_message_t *msg);
pn_data_t *pn_message_annotations(pn_message_t *msg);
pn_data_t *pn_message_properties(pn_message_t *msg);
pn_data_t *pn_message_body(pn_message_t *msg);
int pn_message_decode(pn_message_t *msg, const char *bytes, size_t size);
int pn_message_encode(pn_message_t *msg, char *bytes, size_t *size);
ssize_t pn_message_encode2(pn_message_t *msg, pn_rwbytes_t *buf);
ssize_t pn_message_send(pn_message_t *msg, pn_link_t *sender, pn_rwbytes_t *buf);
int pn_message_data(pn_message_t *msg, pn_data_t *data);
""")

def print_headers(filename):
    with open(filename, 'rt') as f:
        for l in f.readlines():
            pn_extern_ = 'PN_EXTERN '
            if l.startswith(pn_extern_):
                print(l[len(pn_extern_):], end='')

if __name__ == "__main__":
    print_headers('/home/jdanek/repos/qpid/qpid-proton/c/include/proton/message.h')
    ffi.compile(verbose=True, debug=True)
