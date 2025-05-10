import xml.etree.ElementTree as ET

def extrair_dados_xml(conteudo_xml: str) -> dict:
    try:
        root = ET.fromstring(conteudo_xml)
        infos = {
            "cnpj_emitente": root.findtext(".//emit/CNPJ"),
            "nome_emitente": root.findtext(".//emit/xNome"),
            "valor_total": root.findtext(".//vNF"),
            "data_emissao": root.findtext(".//dhEmi"),
        }
        return infos
    except Exception as e:
        return {"erro": f"Erro ao processar XML: {str(e)}"}


