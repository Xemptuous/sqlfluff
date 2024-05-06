"""A List of MariaDB SQL keywords.

https://mariadb.com/kb/en/reserved-words/
"""

mariadb_reserved_keywords = """
ACCESSIBLE
ADD
ALL
ALTER
ANALYZE
AND
AS
ASC
ASENSITIVE
BEFORE
BETWEEN
BIGINT
BINARY
BLOB
BOTH
BY
CALL
CASCADE
CASE
CHANGE
CHANGED_PAGE_BITMAPS
CHAR
CHARACTER
CHECK
CLIENT_STATISTICS
COLLATE
COLUMN
CONDITION
CONSTRAINT
CONTINUE
CONVERT
CREATE
CROSS
CURRENT_DATE
CURRENT_ROLE
CURRENT_TIME
CURRENT_TIMESTAMP
CURRENT_USER
CURSOR
DATABASE
DATABASES
DAY_HOUR
DAY_MICROSECOND
DAY_MINUTE
DAY_SECOND
DEC
DECIMAL
DECLARE
DEFAULT
DELAYED
DELETE
DELETE_DOMAIN_ID
DESC
DESCRIBE
DETERMINISTIC
DISTINCT
DISTINCTROW
DIV
DO_DOMAIN_IDS
DOUBLE
DROP
DUAL
EACH
ELSE
ELSEIF
ENCLOSED
ESCAPED
EXCEPT
EXISTS
EXIT
EXPLAIN
FALSE
FETCH
FLOAT
FLOAT4
FLOAT8
FOR
FORCE
FOREIGN
FROM
FULLTEXT
GENERAL
GRANT
GROUP
HAVING
HIGH_PRIORITY
HOUR_MICROSECOND
HOUR_MINUTE
HOUR_SECOND
IF
IGNORE
IGNORE_DOMAIN_IDS
IGNORE_SERVER_IDS
IN
INDEX
INDEX_STATISTICS
INFILE
INNER
INOUT
INSENSITIVE
INSERT
INT
INT1
INT2
INT3
INT4
INT8
INTEGER
INTERSECT
INTERVAL
INTO
IS
ITERATE
JOIN
KEY
KEYS
KILL
LEADING
LEAVE
LEFT
LIKE
LIMIT
LINEAR
LINES
LOAD
LOCALTIME
LOCALTIMESTAMP
LOCK
LONG
LONGBLOB
LONGTEXT
LOOP
LOW_PRIORITY
MASTER_HEARTBEAT_PERIOD
MASTER_SSL_VERIFY_SERVER_CERT
MATCH
MAXVALUE
MEDIUMBLOB
MEDIUMINT
MEDIUMTEXT
MIDDLEINT
MINUTE_MICROSECOND
MINUTE_SECOND
MOD
MODIFIES
NATURAL
NOT
NO_WRITE_TO_BINLOG
NULL
NUMERIC
OFFSET
ON
OPTIMIZE
OPTION
OPTIONALLY
OR
ORDER
OUT
OUTER
OUTFILE
OVER
PAGE_CHECKSUM
PARSE_VCOL_EXPR
PARTITION
PRECISION
PRIMARY
PROCEDURE
PURGE
RANGE
READ
READS
READ_WRITE
REAL
RECURSIVE
REF_SYSTEM_ID
REFERENCES
REGEXP
RELEASE
RENAME
REPEAT
REPLACE
REQUIRE
RESIGNAL
RESTRICT
RETURN
RETURNING
REVOKE
RIGHT
RLIKE
ROW_NUMBER
ROWS
SCHEMA
SCHEMAS
SECOND_MICROSECOND
SELECT
SENSITIVE
SEPARATOR
SET
SHOW
SIGNAL
SLOW
SMALLINT
SPATIAL
SPECIFIC
SQL
SQLEXCEPTION
SQLSTATE
SQLWARNING
SQL_BIG_RESULT
SQL_CALC_FOUND_ROWS
SQL_SMALL_RESULT
SSL
STARTING
STATS_AUTO_RECALC
STATS_PERSISTENT
STATS_SAMPLE_PAGES
STRAIGHT_JOIN
TABLE
TERMINATED
THEN
TINYBLOB
TINYINT
TINYTEXT
TO
TRAILING
TRIGGER
TRUE
UNDO
UNION
UNIQUE
UNLOCK
UNSIGNED
UPDATE
USAGE
USE
USING
UTC_DATE
UTC_TIME
UTC_TIMESTAMP
VALUES
VARBINARY
VARCHAR
VARCHARACTER
VARYING
WHEN
WHERE
WHILE
WINDOW
WITH
WRITE
XOR
YEAR_MONTH
ZEROFILL
"""

mariadb_unreserved_keywords = """
ACCOUNT
ACTION
ADMIN
AFTER
AGAINST
AGGREGATE
ALGORITHM
ALWAYS
ANY
ASCII
AT
ATOMIC
AUTHORS
AUTO
AUTO_INCREMENT
AUTOEXTEND_SIZE
AVG
AVG_ROW_LENGTH
BACKUP
BEGIN
BINLOG
BIT
BLOCK
BODY
BOOL
BOOLEAN
BTREE
BYTE
CACHE
CASCADED
CATALOG_NAME
CHAIN
CHANGED
CHANNEL
CHARSET
CHECKPOINT
CHECKSUM
CIPHER
CLASS_ORIGIN
CLIENT
CLOB
CLOSE
COALESCE
CODE
COLLATION
COLUMN_NAME
COLUMNS
COLUMN_ADD
COLUMN_CHECK
COLUMN_CREATE
COLUMN_DELETE
COLUMN_GET
COMMENT
COMMIT
COMMITTED
COMPACT
COMPLETION
COMPRESSED
CONCURRENT
CONNECTION
CONSISTENT
CONSTRAINT_CATALOG
CONSTRAINT_NAME
CONSTRAINT_SCHEMA
CONTAINS
CONTEXT
CONTRIBUTORS
CPU
CUBE
CURRENT
CURRENT_POS
CURSOR_NAME
CYCLE
DATA
DATAFILE
DATE
DATETIME
DAY
DEALLOCATE
DEFINER
DELAY_KEY_WRITE
DES_KEY_FILE
DIAGNOSTICS
DIRECTORY
DISABLE
DISCARD
DISK
DO
DUMPFILE
DUPLICATE
DYNAMIC
ELSIF
EMPTY
ENABLE
END
ENDS
ENGINE
ENGINES
ENUM
ERROR
ERRORS
ESCAPE
EVENT
EVENTS
EVERY
EXAMINED
EXCHANGE
EXCLUDE
EXECUTE
EXCEPTION
EXPANSION
EXPIRE
EXPORT
EXTENDED
EXTENT_SIZE
FAST
FAULTS
FEDERATED
FIELDS
FILE
FIRST
FIXED
FLUSH
FOLLOWING
FOLLOWS
FORMAT
FOUND
FULL
FUNCTION
GENERATED
GET_FORMAT
GET
GLOBAL
GOTO
GRANTS
HANDLER
HARD
HASH
HELP
HISTORY
HOST
HOSTS
HOUR
ID
IDENTIFIED
IGNORED
IMMEDIATE
IMPORT
INCREMENT
INDEXES
INITIAL_SIZE
INSERT_METHOD
INSTALL
INVISIBLE
IO
IO_THREAD
IPC
ISOLATION
ISOPEN
ISSUER
INVOKER
JSON
JSON_TABLE
KEY_BLOCK_SIZE
LANGUAGE
LAST
LAST_VALUE
LASTVAL
LEAVES
LESS
LEVEL
LIST
LOCAL
LOCKED
LOCKS
LOGFILE
LOGS
MASTER
MASTER_CONNECT_RETRY
MASTER_DELAY
MASTER_GTID_POS
MASTER_HOST
MASTER_LOG_FILE
MASTER_LOG_POS
MASTER_PASSWORD
MASTER_PORT
MASTER_SERVER_ID
MASTER_SSL
MASTER_SSL_CA
MASTER_SSL_CAPATH
MASTER_SSL_CERT
MASTER_SSL_CIPHER
MASTER_SSL_CRL
MASTER_SSL_CRLPATH
MASTER_SSL_KEY
MASTER_USER
MASTER_USE_GTID
MASTER_DEMOTE_TO_SLAVE
MAX_CONNECTIONS_PER_HOUR
MAX_QUERIES_PER_HOUR
MAX_ROWS
MAX_SIZE
MAX_STATEMENT_TIME
MAX_UPDATES_PER_HOUR
MAX_USER_CONNECTIONS
MEDIUM
MEMORY
MERGE
MESSAGE_TEXT
MICROSECOND
MIGRATE
MINUS
MINUTE
MINVALUE
MIN_ROWS
MODE
MODIFY
MONITOR
MONTH
MUTEX
MYSQL
MYSQL_ERRNO
NAME
NAMES
NATIONAL
NCHAR
NESTED
NEVER
NEXT
NEXTVAL
NO
NOMAXVALUE
NOMINVALUE
NOCACHE
NOCYCLE
NO_WAIT
NOWAIT
NODEGROUP
NONE
NOTFOUND
NUMBER
NVARCHAR
OF
OLD_PASSWORD
ONE
ONLINE
ONLY
OPEN
OPTIONS
ORDINALITY
OTHERS
OVERLAPS
OWNER
PACKAGE
PACK_KEYS
PAGE
PARSER
PATH
PERIOD
PARTIAL
PARTITIONING
PARTITIONS
PASSWORD
PERSISTENT
PHASE
PLUGIN
PLUGINS
PORT
PORTION
PRECEDES
PRECEDING
PREPARE
PRESERVE
PREV
PREVIOUS
PRIVILEGES
PROCESS
PROCESSLIST
PROFILE
PROFILES
PROXY
QUARTER
QUERY
QUERY_RESPONSE_TIME
QUICK
RAISE
RAW
READ_ONLY
REBUILD
RECOVER
REDO_BUFFER_SIZE
REDOFILE
REDUNDANT
RELAY
RELAYLOG
RELAY_LOG_FILE
RELAY_LOG_POS
RELAY_THREAD
RELOAD
REMOVE
REORGANIZE
REPAIR
REPEATABLE
REPLAY
REPLICA
REPLICAS
REPLICA_POS
REPLICATION
RESET
RESTART
RESTORE
RESUME
RETURNED_SQLSTATE
RETURNS
REUSE
REVERSE
ROLE
ROLLBACK
ROLLUP
ROUTINE
ROW
ROWCOUNT
ROWNUM
ROWTYPE
ROW_COUNT
ROW_FORMAT
RTREE
SAVEPOINT
SCHEDULE
SCHEMA_NAME
SECOND
SECURITY
SEQUENCE
SERIAL
SERIALIZABLE
SESSION
SERVER
SETVAL
SHARE
SHUTDOWN
SIGNED
SIMPLE
SKIP
SLAVE
SLAVES
SLAVE_POS
SNAPSHOT
SOCKET
SOFT
SOME
SONAME
SOUNDS
SOURCE
STAGE
STORED
SQL_AFTER_GTIDS
SQL_BEFORE_GTIDS
SQL_BUFFER_RESULT
SQL_CACHE
SQL_NO_CACHE
SQL_THREAD
SQL_TSI_SECOND
SQL_TSI_MINUTE
SQL_TSI_HOUR
SQL_TSI_DAY
SQL_TSI_WEEK
SQL_TSI_MONTH
SQL_TSI_QUARTER
SQL_TSI_YEAR
START
STARTS
STATEMENT
STATUS
STOP
STORAGE
STRING
SUBCLASS_ORIGIN
SUBJECT
SUBPARTITION
SUBPARTITIONS
SUPER
SUSPEND
SWAPS
SWITCHES
SYSDATE
SYSTEM
SYSTEM_TIME
TABLE_NAME
TABLES
TABLESPACE
TABLE_CHECKSUM
TABLE_STATISTICS
TEMPORARY
TEMPTABLE
TEXT
THAN
TIES
TIME
TIMESTAMP
TIMESTAMPADD
TIMESTAMPDIFF
TRANSACTION
TRANSACTIONAL
THREADS
TRIGGERS
TRUNCATE
TYPE
UNBOUNDED
UNCOMMITTED
UNDEFINED
UNDO_BUFFER_SIZE
UNDOFILE
UNICODE
UNKNOWN
UNINSTALL
UNTIL
UPGRADE
USER
USER_RESOURCES
USER_STATISTICS
USER_VARIABLES
USE_FRM
VALIDATION
VALUE
VARCHAR2
VARIABLES
VIA
VIEW
VIRTUAL
VISIBLE
VERSIONING
WAIT
WARNINGS
WEEK
WEIGHT_STRING
WITHIN
WITHOUT
WORK
WRAPPER
X509
XA
XML
YEAR
"""
