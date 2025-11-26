#!/usr/bin/env python3
# Gera iniciante.html completo com 17 nodes no padrão FEP

nodes_data = [
    {"num": 1, "emoji": "⏰", "nome": "Schedule Trigger", "desc": "Automações programadas em horários fixos", "cat": "Trigger", "cor": "emerald", "id": "schedule",
     "topicos": [
         {"titulo": "Intervalos e CRON", "o_que": "Execute workflows a cada X minutos, horas, dias ou use CRON para agendamentos complexos.", "por_que": "Automatize tarefas repetitivas sem intervenção manual (relatórios, backups, sincronizações).", "conceitos": "Intervalos fixos, expressões CRON, timezone, polling schedule."},
         {"titulo": "Configuração de Timezone", "o_que": "Definir o fuso horário correto para garantir execuções no horário local desejado.", "por_que": "Evitar execuções em horários errados, especialmente em equipes globais ou servidores em outras regiões.", "conceitos": "UTC, GMT, timezone local, horário de verão."},
         {"titulo": "Casos de Uso Práticos", "o_que": "Exemplos reais de automações com Schedule Trigger.", "por_que": "Inspirar suas próprias automações vendo aplicações práticas.", "conceitos": "Relatórios diários, backups automáticos, newsletters semanais, monitoramento contínuo."}
     ]},
    {"num": 2, "emoji": "📧", "nome": "Event Trigger", "desc": "Reaja a eventos em tempo real", "cat": "Trigger", "cor": "blue", "id": "event",
     "topicos": [
         {"titulo": "Event vs Schedule Trigger", "o_que": "Event reage a ALGO que acontece (novo email, mensagem); Schedule executa em HORÁRIO fixo.", "por_que": "Entender quando usar cada tipo de trigger é fundamental para automações eficientes.", "conceitos": "Event-driven vs time-based, reatividade, triggers condicionais."},
         {"titulo": "Polling vs Webhook", "o_que": "Polling verifica periodicamente (1 min); Webhook recebe notificação instantânea.", "por_que": "Polling consome execuções; webhook é mais rápido e eficiente.", "conceitos": "Intervalo de polling, execuções, latência, push vs pull."},
         {"titulo": "Apps e Integrações", "o_que": "Gmail, Slack, Google Sheets, Trello e centenas de apps suportados.", "por_que": "Conectar com apps que você já usa diariamente para criar automações poderosas.", "conceitos": "OAuth, credenciais, filtros de eventos, conditions."}
     ]},
    {"num": 3, "emoji": "🪝", "nome": "Webhook", "desc": "Receba dados via HTTP POST/GET", "cat": "API", "cor": "indigo", "id": "webhook",
     "topicos": [
         {"titulo": "O que são Webhooks", "o_que": "Uma URL única que recebe dados de sistemas externos via requisições HTTP.", "por_que": "Integrar N8N com qualquer ferramenta que suporte webhooks, sem polling.", "conceitos": "URL endpoint, métodos HTTP (GET, POST), payload JSON, headers."},
         {"titulo": "Production vs Test URL", "o_que": "Test URL muda a cada ativação do workflow; Production URL é fixa e permanente.", "por_que": "Usar Production URL para integrações reais, Test URL apenas para desenvolvimento.", "conceitos": "Workflow ativo vs inativo, URL persistente, ambiente de teste vs produção."},
         {"titulo": "Respond to Webhook", "o_que": "Enviar resposta de volta para quem chamou o webhook (status 200, dados JSON, etc).", "por_que": "Criar APIs customizadas ou confirmar recebimento de dados.", "conceitos": "Status codes (200, 400, 500), response body, headers customizados."}
     ]},
    {"num": 4, "emoji": "✂️", "nome": "Split Out", "desc": "Divida arrays em items individuais", "cat": "Data", "cor": "green", "id": "split",
     "topicos": [
         {"titulo": "De Array para Items", "o_que": "Transformar 1 item com array de 10 elementos em 10 items separados.", "por_que": "Processar cada elemento individualmente (enviar email para cada pessoa, criar registro por item).", "conceitos": "Field to split out, array destructuring, item count."},
         {"titulo": "Quando Usar", "o_que": "Sempre que API retornar lista e você quiser processar cada elemento individualmente.", "por_que": "Evitar loops manuais, aproveitar processamento paralelo do N8N.", "conceitos": "Batch processing, item-level operations, data normalization."},
         {"titulo": "Split Out vs Loop", "o_que": "Split Out processa todos items em paralelo; Loop processa um por vez sequencialmente.", "por_que": "Escolher a ferramenta certa: paralelo (Split) vs sequencial (Loop).", "conceitos": "Parallel execution, sequential processing, performance trade-offs."}
     ]},
    {"num": 5, "emoji": "🎯", "nome": "Aggregate", "desc": "Agrupe múltiplos items em um só", "cat": "Data", "cor": "green", "id": "aggregate",
     "topicos": [
         {"titulo": "De Items para Array", "o_que": "Oposto do Split Out - combina 100 items em 1 item com array de 100 elementos.", "por_que": "Enviar dados em lote para APIs, criar relatórios consolidados, reduzir número de items.", "conceitos": "Array aggregation, batch operations, data consolidation."},
         {"titulo": "Aggregate All vs By Field", "o_que": "All junta todos em 1; By Field agrupa por categoria (vendas por região, usuários por status).", "por_que": "Criar relatórios agrupados, segmentar dados por critérios específicos.", "conceitos": "Grouping, aggregation strategies, field-based partitioning."},
         {"titulo": "Casos de Uso", "o_que": "Bulk insert em banco de dados, enviar 1000 registros de uma vez, gerar CSV completo.", "por_que": "Otimizar chamadas de API, reduzir custos, melhorar performance.", "conceitos": "Batch API calls, bulk operations, performance optimization."}
     ]},
    {"num": 6, "emoji": "✏️", "nome": "Edit Fields (Set)", "desc": "Crie ou modifique campos de dados", "cat": "Data", "cor": "green", "id": "set",
     "topicos": [
         {"titulo": "Criar e Modificar Campos", "o_que": "Adicionar novos campos, renomear existentes, calcular valores, formatar dados.", "por_que": "Preparar dados para próximos nodes, transformar estrutura de dados, limpar informações.", "conceitos": "Field mapping, data transformation, value assignment."},
         {"titulo": "Expressões e Valores Fixos", "o_que": "Usar valores fixos (\"aprovado\") ou expressões dinâmicas ({{$json.nome.toUpperCase()}}).", "por_que": "Criar campos calculados, concatenar strings, formatar datas, aplicar lógica.", "conceitos": "Expression editor, $json variable, string manipulation, date formatting."},
         {"titulo": "Keep Only Set vs Include Other Fields", "o_que": "Keep Only mantém APENAS campos criados; Include Other preserva campos originais também.", "por_que": "Limpar dados desnecessários ou enriquecer dados existentes.", "conceitos": "Field filtering, data pruning, schema transformation."}
     ]},
    {"num": 7, "emoji": "🔀", "nome": "IF", "desc": "Lógica condicional (se/então)", "cat": "Logic", "cor": "orange", "id": "if",
     "topicos": [
         {"titulo": "True e False Outputs", "o_que": "Direcionar items que atendem condição para True, os demais para False.", "por_que": "Criar fluxos diferentes baseados em critérios (valor > 100, status == \"aprovado\", etc).", "conceitos": "Boolean logic, conditional routing, branching workflows."},
         {"titulo": "Tipos de Condições", "o_que": "String (contains, equals), Number (maior, menor, igual), Boolean, Date comparisons.", "por_que": "Validar dados, filtrar registros, aplicar regras de negócio.", "conceitos": "Operators (==, !=, >, <, contains), data type comparisons, regex matching."},
         {"titulo": "Múltiplas Condições (AND/OR)", "o_que": "Combinar condições - AND (todas devem ser verdade), OR (pelo menos uma verdadeira).", "por_que": "Criar filtros complexos (status == \"ativo\" AND valor > 1000).", "conceitos": "Logical AND, logical OR, condition groups, complex filters."}
     ]},
    {"num": 8, "emoji": "🎚️", "nome": "Switch", "desc": "Roteamento com múltiplas saídas", "cat": "Logic", "cor": "orange", "id": "switch",
     "topicos": [
         {"titulo": "Switch vs IF", "o_que": "IF tem 2 saídas (True/False); Switch tem N saídas (0, 1, 2, 3...).", "por_que": "Rotear para caminhos diferentes baseado em categoria, status, prioridade.", "conceitos": "Multi-way branching, routing rules, fallback output."},
         {"titulo": "Modos de Operação", "o_que": "Rules (condições complexas) ou Expression (retorna número da saída 0-3).", "por_que": "Rules para lógica visual; Expression para cálculos dinâmicos.", "conceitos": "Rule-based routing, expression evaluation, dynamic output selection."},
         {"titulo": "Fallback Output", "o_que": "Saída padrão quando item não atende nenhuma regra.", "por_que": "Garantir que todos items sejam processados, tratar casos não previstos.", "conceitos": "Default routing, error handling, catch-all logic."}
     ]},
    {"num": 9, "emoji": "🔗", "nome": "Merge", "desc": "Combine dados de múltiplas fontes", "cat": "Flow", "cor": "indigo", "id": "merge",
     "topicos": [
         {"titulo": "Modos de Merge", "o_que": "Append (juntar tudo), Combine (mesclar por posição), Match (join por campo-chave).", "por_que": "Enriquecer dados, unir resultados de APIs diferentes, criar datasets completos.", "conceitos": "Append mode, combine by position, key-based matching, left/inner join."},
         {"titulo": "Múltiplas Entradas", "o_que": "Conectar 2+ nodes anteriores ao Merge para combinar seus dados.", "por_que": "Processar dados em paralelo e depois unir resultados.", "conceitos": "Multiple inputs, parallel processing, data synchronization."},
         {"titulo": "Match Fields (JOIN)", "o_que": "Combinar registros que possuem mesmo valor em campo-chave (como SQL JOIN).", "por_que": "Enriquecer dados de clientes com informações de vendas, unir tabelas relacionadas.", "conceitos": "Key fields, inner join, left join, data enrichment."}
     ]},
    {"num": 10, "emoji": "🔁", "nome": "Loop Over Items", "desc": "Processe items sequencialmente em loop", "cat": "Advanced", "cor": "yellow", "id": "loop",
     "topicos": [
         {"titulo": "Loop vs Split Out", "o_que": "Loop processa 1 item por vez em sequência; Split Out processa todos em paralelo.", "por_que": "Use Loop quando ordem importa ou quando precisa de rate limiting.", "conceitos": "Sequential processing, iteration, rate limiting, order preservation."},
         {"titulo": "Batching", "o_que": "Processar X items por vez (ex: 100 de cada vez) ao invés de 1 por 1.", "por_que": "Otimizar performance com batch processing, respeitar limites de API.", "conceitos": "Batch size, pagination, API limits, performance optimization."},
         {"titulo": "Casos de Uso", "o_que": "Rate limiting (max 1 request/segundo), processamento ordenado, wait entre items.", "por_que": "Evitar bloqueios de API, processar grandes volumes gradualmente.", "conceitos": "Throttling, sequential execution, controlled processing."}
     ]},
    {"num": 11, "emoji": "⏸️", "nome": "Wait", "desc": "Pause workflow temporariamente", "cat": "Flow", "cor": "indigo", "id": "wait",
     "topicos": [
         {"titulo": "Tipos de Wait", "o_que": "Duração fixa (5 segundos), Até data específica, Aguardar webhook/evento.", "por_que": "Rate limiting, aguardar processamento externo, workflows multi-etapa.", "conceitos": "Time-based wait, event-based wait, resumable workflows."},
         {"titulo": "Wait for Webhook", "o_que": "Pausar workflow até receber resposta via webhook (aprovação, confirmação).", "por_que": "Criar workflows com interação humana, processos de aprovação.", "conceitos": "Human-in-the-loop, approval workflows, webhook resume."},
         {"titulo": "Limites e Timeouts", "o_que": "Máximo de espera (timeout após 7 dias), limites de execuções simultâneas aguardando.", "por_que": "Planejar workflows de longa duração, entender custos e limites.", "conceitos": "Execution limits, timeout handling, long-running workflows."}
     ]},
    {"num": 12, "emoji": "🌐", "nome": "HTTP Request", "desc": "Conecte com qualquer API REST", "cat": "API", "cor": "pink", "id": "http",
     "topicos": [
         {"titulo": "Métodos HTTP", "o_que": "GET (buscar), POST (criar), PUT/PATCH (atualizar), DELETE (remover).", "por_que": "Integrar com qualquer API REST do mercado.", "conceitos": "REST methods, CRUD operations, idempotency."},
         {"titulo": "Autenticação", "o_que": "Bearer Token, API Key, Basic Auth, OAuth2.", "por_que": "Acessar APIs protegidas com segurança.", "conceitos": "Authentication methods, API keys, OAuth flows, headers."},
         {"titulo": "Headers e Body", "o_que": "Headers (Content-Type, Authorization), Body (JSON, Form, Raw).", "por_que": "Configurar requisições corretamente, enviar dados estruturados.", "conceitos": "HTTP headers, request body, JSON payload, content types."}
     ]},
    {"num": 13, "emoji": "💻", "nome": "Code", "desc": "Execute JavaScript/Python custom", "cat": "Advanced", "cor": "yellow", "id": "code",
     "topicos": [
         {"titulo": "JavaScript e Python", "o_que": "Executar código customizado quando nodes visuais não são suficientes.", "por_que": "Fazer transformações complexas, cálculos avançados, lógica personalizada.", "conceitos": "JavaScript runtime, Python support, custom logic."},
         {"titulo": "Run Once vs Run for Each Item", "o_que": "Run Once para todos items; Run for Each processa item por item.", "por_que": "Escolher modo correto conforme necessidade (agregação vs transformação individual).", "conceitos": "Execution modes, $input.all() vs $input.item, item iteration."},
         {"titulo": "Bibliotecas e Limitações", "o_que": "Bibliotecas incluídas (luxon, axios), sandbox seguro, timeout de execução.", "por_que": "Entender capacidades e restrições do ambiente de execução.", "conceitos": "Built-in libraries, sandbox environment, execution timeout."}
     ]},
    {"num": 14, "emoji": "🔄", "nome": "Execute Workflow", "desc": "Chame outros workflows", "cat": "Flow", "cor": "indigo", "id": "execute",
     "topicos": [
         {"titulo": "Modularização", "o_que": "Dividir workflows grandes em módulos menores reutilizáveis.", "por_que": "Manter código organizado, reutilizar lógica comum, facilitar manutenção.", "conceitos": "Sub-workflows, reusability, modular design."},
         {"titulo": "Passagem de Dados", "o_que": "Enviar dados para workflow filho, receber resultado de volta.", "por_que": "Criar workflows parametrizáveis, implementar funções reutilizáveis.", "conceitos": "Input data, return values, workflow parameters."},
         {"titulo": "Wait for Completion", "o_que": "Aguardar workflow terminar (síncrono) ou disparar e continuar (assíncrono).", "por_que": "Controlar execução, processar resultados ou disparar fire-and-forget.", "conceitos": "Synchronous execution, asynchronous calls, workflow orchestration."}
     ]},
    {"num": 15, "emoji": "⚠️", "nome": "Error Trigger", "desc": "Capture e trate erros de workflows", "cat": "Advanced", "cor": "yellow", "id": "error",
     "topicos": [
         {"titulo": "Workflow de Tratamento", "o_que": "Workflow separado que é executado quando outro workflow falha.", "por_que": "Log de erros, notificações, retry automático, monitoramento centralizado.", "conceitos": "Error handling, workflow monitoring, failure recovery."},
         {"titulo": "Dados do Erro", "o_que": "Recebe informações sobre erro (mensagem, stack trace, workflow, node).", "por_que": "Debug eficiente, criar alertas contextualizados, análise de falhas.", "conceitos": "Error metadata, stack traces, execution context."},
         {"titulo": "Casos de Uso", "o_que": "Enviar email quando workflow falha, salvar log em banco, notificar Slack.", "por_que": "Monitoramento proativo, SLA compliance, operação profissional.", "conceitos": "Error notifications, logging, incident management."}
     ]},
    {"num": 16, "emoji": "↩️", "nome": "Respond to Webhook", "desc": "Envie resposta de volta ao webhook", "cat": "API", "cor": "pink", "id": "respond",
     "topicos": [
         {"titulo": "Status Codes", "o_que": "Retornar status HTTP correto (200 sucesso, 400 erro, 500 falha).", "por_que": "Comunicar resultado da operação para sistema chamador.", "conceitos": "HTTP status codes, success/error responses, API standards."},
         {"titulo": "Response Body e Headers", "o_que": "Enviar dados JSON, configurar headers customizados (Content-Type, CORS).", "por_que": "Criar APIs completas com N8N, integrações bidirecionais.", "conceitos": "Response payload, custom headers, CORS configuration."},
         {"titulo": "Respond Imediatamente vs Após Processamento", "o_que": "Responder antes de processar (202 Accepted) ou após completar workflow.", "por_que": "Evitar timeouts, implementar processamento assíncrono.", "conceitos": "Async processing, early response, timeout prevention."}
     ]},
    {"num": 17, "emoji": "🤖", "nome": "AI Agent", "desc": "Crie agentes inteligentes com ferramentas", "cat": "AI", "cor": "purple", "id": "agent",
     "topicos": [
         {"titulo": "Agent vs Chat Model", "o_que": "Chat Model apenas conversa; Agent pode usar TOOLS (buscar dados, executar ações).", "por_que": "Criar assistentes que interagem com sistemas reais, não só conversam.", "conceitos": "Tool calling, function calling, agentic behavior."},
         {"titulo": "Tools (Ferramentas)", "o_que": "Conectar sub-workflows que AI pode chamar (buscar cliente, criar ticket, enviar email).", "por_que": "Dar superpoderes para AI interagir com seus sistemas.", "conceitos": "Tool definition, workflow tools, AI function calling."},
         {"titulo": "System Prompt e Configuração", "o_que": "Instruções de comportamento, escolha de modelo (GPT-4, Claude), temperatura, tokens.", "por_que": "Controlar personalidade e capacidades do agent.", "conceitos": "System prompts, model selection, temperature, max tokens."}
     ]},
]

# Gerar HTML para cada node
def gerar_node_html(node):
    topicos_html = ""
    for topico in node["topicos"]:
        topicos_html += f'''
        <li class="topic-item">
          <button class="topic-button w-full text-left px-4 py-1 bg-neutral-50 dark:bg-neutral-700 hover:bg-neutral-100 dark:hover:bg-neutral-600 rounded-lg transition-colors font-medium text-neutral-800 dark:text-neutral-200">
            📌 {topico["titulo"]}
          </button>
          <div class="topic-explanation hidden ml-6 mt-2 p-4 bg-{node["cor"]}-50 dark:bg-{node["cor"]}-900/20 rounded-lg border-l-4 border-{node["cor"]}-500">
            <p class="text-sm mb-1.5 text-neutral-700 dark:text-neutral-300">
              <strong class="text-{node["cor"]}-600">O que é:</strong> {topico["o_que"]}
            </p>
            <p class="text-sm mb-1.5 text-neutral-700 dark:text-neutral-300">
              <strong class="text-{node["cor"]}-600">Por que aprender:</strong> {topico["por_que"]}
            </p>
            <p class="text-sm text-neutral-700 dark:text-neutral-300">
              <strong class="text-{node["cor"]}-600">Conceitos chave:</strong> {topico["conceitos"]}
            </p>
          </div>
        </li>'''

    return f'''
    <!-- Node {node["num"]}: {node["nome"]} -->
    <div class="module-card bg-white dark:bg-neutral-800 rounded-xl shadow-md p-6">
      <div class="flex items-center justify-between mb-4">
        <div class="flex items-center gap-3">
          <span class="text-4xl">{node["emoji"]}</span>
          <div>
            <h2 class="text-2xl font-bold text-neutral-900 dark:text-neutral-100">{node["num"]}. {node["nome"]}</h2>
            <p class="text-sm text-neutral-600 dark:text-neutral-400">{node["desc"]}</p>
          </div>
        </div>
        <span class="px-3 py-1 bg-{node["cor"]}-100 dark:bg-{node["cor"]}-900/30 text-{node["cor"]}-800 dark:text-{node["cor"]}-300 rounded-full text-xs font-semibold">
          {node["cat"]}
        </span>
      </div>

      <ul class="topics-list space-y-0.5">{topicos_html}
      </ul>

      <div class="mt-4 pt-4 border-t border-neutral-200 dark:border-neutral-700 flex gap-2">
        <button onclick="openModal('modal-{node["id"]}')" class="bg-emerald-600 hover:bg-emerald-700 text-white px-3 py-2 rounded-lg text-sm font-semibold transition-colors">
          📖 Ver em Modal
        </button>
        <a href="conteudo/{node["id"]}.html" class="bg-blue-600 hover:bg-blue-700 text-white px-3 py-2 rounded-lg text-sm font-semibold transition-colors">
          📄 Página Completa
        </a>
        <a href="downloads/{node["id"]}.md" download class="bg-neutral-600 hover:bg-neutral-700 text-white px-3 py-2 rounded-lg text-sm font-semibold transition-colors">
          📥 Download MD
        </a>
      </div>
    </div>
'''

# Gerar todos os nodes
all_nodes_html = "\n".join([gerar_node_html(n) for n in nodes_data])

# Salvar em arquivo temporário
with open('/home/nmaldaner/projetos/N8Nb/nodes_section.html', 'w') as f:
    f.write(all_nodes_html)

print(f"✅ Gerados {len(nodes_data)} nodes HTML")
print("Arquivo salvo em: nodes_section.html")
