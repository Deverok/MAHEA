/** MAHEA shared interface shapes (documentation-only; no build required). */

export type CapabilityKind = 'hook' | 'tool' | 'plugin' | 'skill';

export interface TurnInput {
  message: string;
  metadata?: Record<string, unknown>;
}

export interface TurnResult {
  output: string;
  steps?: unknown[];
}

export interface Kernel {
  boot(): void;
  shutdown(): void;
  handleTurn(input: TurnInput): TurnResult;
  registerCapability(kind: CapabilityKind, handler: unknown): void;
}

export interface ContextLayer {
  buildContext(turn: TurnInput): unknown;
  trimContext(context: unknown, budget: number): unknown;
}

export interface OrchestrationLayer {
  plan(goal: string, context: unknown): unknown;
  nextStep(state: unknown): unknown;
  runLoop(loopDef: unknown): unknown;
  runGraph(graphDef: unknown): unknown;
}

export interface ActionLayer {
  executeAction(planStep: unknown): unknown;
  requestApproval(action: unknown): boolean;
}

export interface ModelAdapter {
  complete(request: unknown): unknown;
}

export interface InteropAdapter {
  translateInbound(message: unknown): unknown;
  translateOutbound(message: unknown): unknown;
}

export interface PolicyDecision {
  allow: boolean;
  reason?: string;
}
