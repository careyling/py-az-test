CREATE OR REPLACE FUNCTION FN_HTTP_GET (v_url VARCHAR2) 
RETURN VARCHAR2 
AS 
BEGIN 
 DECLARE
 req UTL_HTTP.REQ;
 resp UTL_HTTP.RESP;
 v_line VARCHAR2 ( 4000 );
 v_text VARCHAR2 ( 4000 );
 BEGIN
  v_text := '';
  BEGIN
    req := UTL_HTTP.BEGIN_REQUEST ( url => v_url, method => 'GET' );
    UTL_HTTP.SET_BODY_CHARSET('UTF-8');
    UTL_HTTP.SET_HEADER(req, 'Content-Type', 'application/x-www-form-urlencoded');
    resp := UTL_HTTP.GET_RESPONSE ( req );
    LOOP
     UTL_HTTP.READ_LINE ( resp, v_line, TRUE );
     v_text := v_text || v_line;
    END LOOP;
  UTL_HTTP.END_RESPONSE( resp );
  UTL_HTTP.END_REQUEST( req );
 EXCEPTION
   WHEN UTL_HTTP.END_OF_BODY THE
   UTL_HTTP.END_RESPONSE ( resp );
   WHEN OTHERS THEN
   UTL_HTTP.END_RESPONSE(resp)
   UTL_HTTP.END_REQUEST(req);
  END;
 return v_text;
END;
END;